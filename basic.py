#!/usr/bin/env python3

#####################################################################
# This script presents how to use the most basic features of the environment.
# It configures the engine, and makes the agent perform random actions.
# It also gets current state and reward earned with the action.
# <episodes> number of episodes are played. 
# Random combination of buttons is chosen for every action.
# Game variables from state and last reward are printed.
#
# To see the scenario description go to "../../scenarios/README.md"
#####################################################################

from __future__ import print_function
import vizdoom as vzd

from random import choice
from time import sleep, time
import numpy as np

if __name__ == "__main__":
    game = vzd.DoomGame()
    game.set_doom_scenario_path("scenarios/basic.wad")
    game.set_doom_map("map01")

    game.set_screen_resolution(vzd.ScreenResolution.RES_640X480)
    game.set_screen_format(vzd.ScreenFormat.RGB24)
    game.set_depth_buffer_enabled(True)
    game.set_labels_buffer_enabled(True)
    game.set_automap_buffer_enabled(True)
    game.set_objects_info_enabled(True)
    game.set_sectors_info_enabled(True)

    game.set_render_hud(False)
    game.set_render_minimal_hud(False)  # If hud is enabled
    game.set_render_crosshair(False)
    game.set_render_weapon(True)
    game.set_render_decals(False)  # Bullet holes and blood on the walls
    game.set_render_particles(False)
    game.set_render_effects_sprites(False)  # Smoke and blood
    game.set_render_messages(False)  # In-game messages
    game.set_render_corpses(False)
    game.set_render_screen_flashes(True)  # Effect upon taking damage or picking up items

    game.add_available_button(vzd.Button.MOVE_LEFT)
    game.add_available_button(vzd.Button.MOVE_RIGHT)
    game.add_available_button(vzd.Button.ATTACK)

    game.add_available_game_variable(vzd.GameVariable.AMMO2)

    game.set_episode_timeout(200)

    game.set_episode_start_time(10)

    game.set_window_visible(True)
    # game.set_sound_enabled(True)

    game.set_living_reward(-1)

    game.set_mode(vzd.Mode.PLAYER)

    game.init()

    # MOVE_LEFT, MOVE_RIGHT, ATTACK
    actions = [[True, False, False], [False, True, False], [False, False, True]]

    episodes = 100

    sleep_time = 1.0 / vzd.DEFAULT_TICRATE  # = 0.028

    all_start = time()
    per_episode = []
    neg = 0
    for i in range(episodes):
        print("Episode #" + str(i + 1))

        game.new_episode()
        episode_start = time()
        while not game.is_episode_finished():
            state = game.get_state()

            n = state.number
            vars = state.game_variables
            screen_buf = state.screen_buffer
            depth_buf = state.depth_buffer
            labels_buf = state.labels_buffer
            automap_buf = state.automap_buffer
            labels = state.labels
            objects = state.objects
            sectors = state.sectors

            r = game.make_action(choice(actions))
            
            if sleep_time > 0:
                sleep(sleep_time)

        episode_end = time()
        per_episode.append(episode_end - episode_start)
        
        print("Episode finished.")
        print("Total reward:", game.get_total_reward())
        print("************************")
        if game.get_total_reward() < 0:
            neg += 1
    all_end = time()
    print('Negatives: {}'.format(neg))
    print('Elapset per episode: {}'.format(np.mean(np.asarray(per_episode))))
    print('Elapset total: {}'.format(all_end - all_start))

    game.close()
