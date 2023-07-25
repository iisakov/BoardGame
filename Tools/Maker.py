from datetime import date

import Components


class Maker:
    @staticmethod
    def make_standard_game(gif_speed: int or list, game_num, size=50):
        for i in range(game_num):

            frames = []
            game = Components.BoardGame(num_players=4, num_gex_in_hand=2, num_steps=7, size=size)
            root_path_game_img = f'static/{date.today()}/img/game_{i + 1}'
            root_path_game_gif = f'static/{date.today()}/gif/game_{i + 1}'
            game.start().print_map_on_board().add_frame(frames).safe_board('initial_map', root_path_game_img)
            game_round_num = 0
            while game.get_num_gex_in_deck() > 0:
                game_round_num += 1
                for player in game.get_players():
                    for _ in range(game.get_num_gex_in_hand()):
                        player.take_gex_in_hand(game.get_deck().pull_gex())

                for player in game.get_players():
                    player_move_num = 0
                    while player.get_num_gex_in_hand() > 0:
                        player_move_num += 1
                        deployed = player.deploy_gex(game.get_map())
                        if not deployed:
                            game.get_discard().push_gex(player.discard_active_gex())
                        game.print_add_safe(frames, f'move_{player_move_num}', root_path_game_img + f'/map_by_moves/move_{game_round_num}/{player.get_name()}')
                    game.print_safe('finished_map', root_path_game_img + f'/map_by_moves/move_{game_round_num}/{player.get_name()}')
                game.print_safe('finished_map', root_path_game_img + f'/map_by_moves/move_{game_round_num}')
            game.print_safe('finished_map', root_path_game_img)

            for speed in gif_speed if type(gif_speed) == list else range(1):
                speed = speed if type(gif_speed) == list else gif_speed
                game.make_gif(frames, speed, f'finished_map_speed_{speed}', root_path_game_gif)
    @staticmethod
    def make_request_game(num_players, num_gex_in_hand, size=50):
        frames = []
        game = Components.BoardGame(num_players=num_players, num_gex_in_hand=num_gex_in_hand, num_steps=7, size=size)
        root_path_game_img = f'static/requested_game/img/game'
        root_path_game_gif = f'static/requested_game/gif/game'
        game.start().print_map_on_board().add_frame(frames).safe_board('initial_map', root_path_game_img)
        game_round_num = 0
        while game.get_num_gex_in_deck() > 0:
            game_round_num += 1
            for player in game.get_players():
                for _ in range(game.get_num_gex_in_hand()):
                    player.take_gex_in_hand(game.get_deck().pull_gex())

            for player in game.get_players():
                player_move_num = 0
                while player.get_num_gex_in_hand() > 0:
                    player_move_num += 1
                    deployed = player.deploy_gex(game.get_map())
                    if not deployed:
                        game.get_discard().push_gex(player.discard_active_gex())
                    game.print_add_safe(frames, f'move_{player_move_num}', root_path_game_img + f'/map_by_moves/move_{game_round_num}/{player.get_name()}')
                game.print_safe('finished_map', root_path_game_img + f'/map_by_moves/move_{game_round_num}/{player.get_name()}')
            game.print_safe('finished_map', root_path_game_img + f'/map_by_moves/move_{game_round_num}')
        game.print_safe('finished_map', root_path_game_img)

        game.make_gif(frames, 100, f'finished_map', root_path_game_gif)
