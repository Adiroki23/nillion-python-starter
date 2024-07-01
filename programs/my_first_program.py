from nada_dsl import *

def nada_main():
    # Define the parties (players)
    player1 = Party(name="Player1")
    player2 = Party(name="Player2")
    player3 = Party(name="Player3")

    # Secret guesses from each player
    guess1 = SecretInteger(Input(name="guess1", party=player1))
    guess2 = SecretInteger(Input(name="guess2", party=player2))
    guess3 = SecretInteger(Input(name="guess3", party=player3))

    # Secret target number (this could also be an input from a secure source)
    target = SecretInteger(Constant(50))

    # Calculate the absolute differences from the target
    diff1 = abs(guess1 - target)
    diff2 = abs(guess2 - target)
    diff3 = abs(guess3 - target)

    # Determine the closest guess
    closest_guess = If(diff1 < diff2, If(diff1 < diff3, guess1, guess3), If(diff2 < diff3, guess2, guess3))

    # Output the closest guess to each player
    return [Output(closest_guess, "closest_guess_output", player1),
            Output(closest_guess, "closest_guess_output", player2),
            Output(closest_guess, "closest_guess_output", player3)]

