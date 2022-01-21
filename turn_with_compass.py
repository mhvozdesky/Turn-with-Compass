def direction(facing, turn):

    directions = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
    
    position_index = directions.index(facing)
    
    final_position_index = int((position_index + (turn / 45)) % 8)
    
    return directions[final_position_index]


if __name__ == '__main__':
    
    print(direction('S', 180))
    
    assert direction('S', 180) == 'N'
    assert direction('SE', -45) == 'E'
    assert direction('W', 495) == 'NE'
