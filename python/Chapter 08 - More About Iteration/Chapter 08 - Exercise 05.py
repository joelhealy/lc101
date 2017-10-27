#  Here’s the start of a program for a weight training app that coaches users
#  on how much weight they should lift for each of these three lifts: squat,
#  bench, and deadlift. The program begins by having the user lift only 10
#  pounds for each lift. Each time they complete a set for a particular lift
#  and say they are ready for the next set, add 10 pounds to the weight of
#  their previous set and print a message that this is the new weight they
#  should lift. The sets are all done for one lift at a time. So, for example,
#  a user might squat 10 pounds, then 20 pounds, then 30 pounds and then say
#  they don’t want to keep doing that lift. In this case, they’ll now get a
#  printed message to bench 10 pounds, and so on and so forth.
#
#  Some of the code is already included below, but you will need to fill in the
#  rest of the main function to produce the following functionality:
#
#      For each lift, beginning with the squat, the function workout_coach
#      should be called with the name of the lift and the current weight.
#      This function prints a message to the user like the following:
#
#      Time to squat 10 pounds! You got this!
#
#      Keep calling workout_coach for as long as the user answers “yes” to the
#      following question: “Keep doing the squat? Enter yes for the next set.”
#      (Note that you will need to fill in the name of the lift depending on
#      which lift in the iteration they are on.) You can do something like the
#      following to combine strings and a variable to create the prompt string:
#
#          input_prompt = "Keep doing the " + lift +
#                         "? Enter yes for the next set."
#
#      If the user answers with anything besides “yes” to the above question,
#      then stop calling workout_coach for that particular lift and move on to
#      repeat the above process for the next lift (unless it is the deadlift,
#      which is the last lift and thus once the user decides to stop at this
#      point the program quits).
#      There is one special case where you should stop calling workout_coach
#      — no matter what the user responds — and that is when the current weight
#      is greater than 200 pounds for the bench. You have not yet talked with a
#      lawyer about your app and you don’t want to get sued if anyone has a
#      mishap, so you’re not going to encourage them to lift more than that
#      amount of weight on the bench press (which is the exercise that, done
#      improperly and without a spotter, causes most gym accidents). It is okay
#      to keep encouraging users to lift more than 200 pounds for the squat and
#      the deadlift, though, so you don’t need to set an upper limit for those
#      lifts.
#
#  Here is some example output from a program run:
#
#      Time to squat 10 pounds! You got this!
#      Time to squat 20 pounds! You got this!
#      Time to bench 10 pounds! You got this!
#      Time to bench 20 pounds! You got this!
#      Time to bench 30 pounds! You got this!
#      Time to deadlift 10 pounds! You got this!
#      Time to deadlift 20 pounds! You got this!
#      Time to deadlift 30 pounds! You got this!
#      Time to deadlift 40 pounds! You got this!
#

import sys


def workout_coach(lift_name, wt):
    print("Time to", lift_name, wt, "pounds! You got this!")


def main():
    sys.setExecutionLimit(120000)  # keep program from timing out
    lifts = ["squat", "bench", "deadlift"]
    for lift in lifts:
        print()
        weight = 10
        answer = 'yes'
        while answer == 'yes':
            if lift == 'bench' and weight > 200:
                print("Sorry, you need to move on to something different.")
                break
            workout_coach(lift, weight)
            input_prompt = "Keep doing the " + lift \
                + "? Enter yes for the next set.  "
            answer = input(input_prompt)
            weight += 10


if __name__ == "__main__":
    main()
