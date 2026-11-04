# Coding Standards

## Scope & discoverability
- This document is canonical in `JollyGreenFrogs/frogsense` (`docs/coding-standards.md`); every other repo keeps a synced copy or links to it
- Enterprise distribution: the org-wide copy lives in `JollyGreenFrogs/.github` (`coding-standards.md` + `copilot-instructions.md` template); each repo carries `docs/coding-standards.md` and `.github/copilot-instructions.md`, synced from there
- Every repo's CONTRIBUTING/README links here; agents and humans read this doc before editing code in any repo

## Architecture Design Documents (ADRs / ADDs)
- New flows/architecture get an **ADD before code** — one file per decision (`docs/architecture/ADR-NNN-title.md`), indexed in `decisions.md`. House format is the ADD style: Context → Design → Decision → Rejected Alternatives → Consequences; **Design comes before Decision**, and the file is a living doc that evolves as the build evolves
- The **Decision section is immutable once filed** — to change a decision, write a new ADD and mark the old one `Superseded by ADR-NNN`. Rejected alternatives are recorded in the ADD
- Status lifecycle: `Proposed | Draft` → `Accepted | Rejected` → `Implemented` → `Deprecated | Superseded` (the last state only happens when a later ADD updates/grows the decision)

## Git / Commits
- **Conventional Commits**: `feat:`, `fix:`, `chore:`, `docs:`, `refactor:`, etc.
- **Git flow** branching — `feature/`, `bugfix/`, `release/`, `hotfix/` from `develop`
- PRs required for `main` and `develop`; no direct pushes; 1 approving review
- **NEVER deploy from a feature branch** — merge first, deploy from `develop` or `main`

## Branch topology for big rewrites
- One **epic branch** per rewrite (e.g. `feature/sage-tool-control`); task branches per PR with the epic as base; `develop` only when the full rewrite is done (may be a force-merge, decided then)

## Paradigm
- **Functions are the default; classes are the exception.** Before writing a class, name which allowed use below it falls under — if you can't, write a function.
- Allowed classes, exhaustively:
  1. **Data models** — Pydantic / dataclasses: fields + validation only, **no business-logic methods** (derived properties OK)
  2. **State holders** — singletons/services with lifecycle state (e.g. `VaultClient`, DB connections). Prefer passing state explicitly as a function argument; a module-level instance lives only at the composition root (app startup)
  3. **100%-required bases** — where a framework/library forces a class: LangChain `BaseChatModel`, ASGI apps, ORM/DB-driver bases, exception classes. Note the requirement in a comment
- **No inheritance hierarchies, mixins, or ABCs** beyond the above — compose with dataclasses/Pydantic instead. Prefer closures / `functools.partial` over callable classes. Carve-out: ORM mixins are allowed **inside `database_models/` only** (a database concern)
- Placement of allowed classes:
  - Data models (Pydantic/dataclasses) → `data_models/` package (`models.py` only as a time-boxed migration shim)
  - ORM models → `database_models/` package
  - DB/connection classes → the relevant database module
  - Service singletons → their own module

## Functions
- Functions should **do one thing only** — no multi-responsibility functions
- Minimise branching and alternative code paths where possible
- Helper/utility functions live in **dedicated utils or helper modules**, split by what they do (e.g. `utils/text.py`, `utils/http.py`) — not scattered across feature modules

## Imports
- All imports at the **top of the file** — no inline imports
- One accepted exception: genuine circular dependencies (document the reason with a comment)

## Docstrings & readability
- Every function gets a docstring that explains **what it does and every parameter** — Args (name + meaning, incl. optional/control params), Returns, Raises (incl. whether CancelledError propagates), and a pointer to the governing ADR/review when non-obvious
- Module docstrings state scope + invariants (privacy rules, no function-level imports, which ADR owns the behavior)
- Log only coarse categories (never raw model output / response bodies / user text — PR #112 review)
- Code should read top-down: small functions, one concern each, docstrings carry the "why" that isn't obvious from the code

## File & module layout
- **One module per concern** — group by what it does, not by which route uses it (e.g. `data_models/search.py` is reusable by any route that searches)
- **No mixed concerns in one file** — a file is either data (models only) or behavior (functions/service), never both: never put a data class in the same file as a service or function. Private `_`-prefixed helper **functions** may stay co-located with their single caller — but never single-use private **classes** (e.g. a one-off exception): shared exception types live in the package's `errors.py` — or next to the single service/class that owns them; if nothing outside the file needs it, raise a built-in (`ValueError`, `RuntimeError`, …) instead
- **Small files** — target < ~200 lines per file (house rule, ADR-056); applies to **new code and any file you touch** — legacy oversized files are split when modified (characterization tests first), never in unrelated PRs; split into a sub-package when a module grows past it
- **Models live only in the model packages** — `data_models/` for Pydantic/dataclass DTOs, `database_models/` for ORM models — never inside feature/route packages; those packages must never import from feature code (no import cycles)
- **No re-export shims for internal moves** — move + update all import sites atomically. Exception: a **time-boxed migration shim** during an active rewrite, with a tracking issue and removal date; shims for public/external surfaces are permanent

## Database access
- New code in the main app uses the **ORM** (SQLAlchemy `ViraBase`) — no raw SQL
- Exception on record: `vira_memory_service` is raw sqlcipher3 until its dedicated ORM-swap ADR lands — new code there follows the existing raw convention, and the swap is one coherent change, never per-PR hybrids

## Secrets & user-data privacy
- Secrets live in **Vault / env only — never in the DB**
- Raw user content never goes to system stores (`__vira__`): user data lives only in the user's own encrypted DB; durable rows are redacted (hashes/metrics); full text is transient-only and purged **service-side** (scheduled sweep + on activity), not just on read

## Prompts & runtime config
- **All model-facing prompt text lives in the prompt library** (KG prompt-module rows in `__vira__`); code constants are fallback seeds only
- Runtime knobs are **env-only** until the DB-backed config ADR is approved

## Testing
- **Zero test regressions** — characterization tests pin legacy behavior *before* rewiring it
- Byte-compile gate: a suite test runs `compileall` over all source dirs so syntax errors fail CI even in unimported modules
- Run the full unit suite before every push; e2e separately against the deployed UAT

## Commit format
- Conventional Commits, and every commit ends with the trailer:
  ```
  Generated by Mistral Vibe.
  Co-Authored-By: Mistral Vibe <vibe@mistral.ai>
  ```

## CI
- **Woodpecker only** (`.woodpecker.yml`): unit tests gate every push/PR; branch pushes deploy UAT/prod. Do **not** duplicate this in GitHub Actions — GitHub is for PRs + review bot only

## AI-assisted development workflow (Mistral Vibe / Copilot-style agents)
- **Show code before writing it** — the operator reviews the exact diff first; no code lands without approval
- **Material changes require explicit approval**; small review-comment fixes within an approved scope may proceed, and are listed in the summary so they can be vetoed
- Process loop: show → approve → implement + test → commit + push → resolve review threads → repeat
- The agent never merges/closes PRs and never pushes to protected branches; force-push only with explicit per-case approval (`--force-with-lease` preferred)
- **Deploys need explicit per-occurrence approval** — "deploy" is never implied by a merge
- Risk acceptance is the operator's RAID entry only — agents never write "accepted risk" into docs

## Review presentation (operator preference)
- Short sections, tables, flow diagrams, code blocks, side-by-side comparisons — one question at the end. No walls of prose.

## References (external grounding)
- GoF, *Design Patterns* (1994) — favor composition over inheritance → Paradigm rules
- Wlaschin, *Domain Modeling Made Functional* — functional core, imperative shell → classes only at the edges (state/I-O)
- Martin, *Clean Code* — SRP, small functions → Functions / small files
- PEP 8 / PEP 257 + Google Python Style Guide — imports at top; docstring Args/Returns/Raises
- conventionalcommits.org v1.0.0 — commit types
- Driessen, "A successful Git branching model" (nvie.com, 2010) — git flow
- Nygard ADR (2011) / adr.github.io — ADR lifecycle (our ADD lifecycle extends it: `Draft`/`Implemented` + living-doc format are house additions)
- 12factor.net §III + OWASP cheat sheets — config/secrets in env or Vault, never in code/DB
- Feathers, *Working Effectively with Legacy Code* (2004) — characterization tests
- **House decisions with no external authority** (do not cite as external standards): the ~200-line file threshold, exception placement, the ADD status lifecycle, Woodpecker-only CI
