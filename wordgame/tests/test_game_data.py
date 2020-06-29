import game_data as gd


def test_create_class_number_rounds():

    game_class = gd.game_data()

    assert game_class.number_rounds == 0 
    #if game_class.number_rounds == 0:
    #    print("got it right")
    #else:
    #    print("got it wrong!!!")
