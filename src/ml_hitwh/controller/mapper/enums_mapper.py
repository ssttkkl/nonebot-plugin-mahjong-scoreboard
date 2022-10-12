from ml_hitwh.model.enums import PlayerAndWind, GameState

player_and_wind_mapping = {
    PlayerAndWind.four_men_east: '四人东',
    PlayerAndWind.four_men_south: '四人南'
}

game_state_mapping = {
    GameState.uncompleted: '未完成',
    GameState.completed: '已完成',
    GameState.invalid_total_point: '分数冲突'
}