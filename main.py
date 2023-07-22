import datetime

import Components
import Tools.Printer

low_speed = 1500
high_speed = 200
count = 1
size = 50

game_num = 10
for day in range(10):
    for i in range(game_num):
        frames = []
        print('day:', day, 'game_name', i)
        game = Components.BoardGame(num_players=4, num_gex_in_hand=2, size=size)
        root_path_game_img = f'static/{datetime.date.today()-datetime.timedelta(day)}/img/game_{i+1}'
        root_path_game_gif = f'static/{datetime.date.today()-datetime.timedelta(day)}/gif/game_{i+1}'
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
                    game.print_map_on_board().add_frame(frames).safe_board(f'move_{player_move_num}', root_path_game_img + f'/map_by_moves/move_{game_round_num}/{player.get_name()}')
                    print(day, i, player.get_name(), deployed)
                game.print_map_on_board().safe_board('finished_map', root_path_game_img + f'/map_by_moves/move_{game_round_num}/{player.get_name()}')
            game.print_map_on_board().safe_board('finished_map', root_path_game_img + f'/map_by_moves/move_{game_round_num}')
        game.print_map_on_board().safe_board('finished_map', root_path_game_img)

        game.make_gif(frames, low_speed, 'finished_map_low_speed', root_path_game_gif)
        game.make_gif(frames, high_speed, 'finished_map_high_speed', root_path_game_gif)

if __name__ == '__main__':
    pass
