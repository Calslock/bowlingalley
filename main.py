import tkinter as tk

main_page = tk.Tk()
main_page.geometry("380x120")
main_page.title("BowlingAlley")


def calculate_points(result: list) -> list:
    print("Przebieg gry: ", result)
    points = 0
    point_list = []
    last_frame = result[len(result) - 1]

    for frame in range(len(result)-1):
        try:
            if result[frame][0] == 'X':
                points += 10
                if result[frame+1][0] == 'X':
                    points += 10
                    if result[frame+2][0] == 'X':
                        points += 10
                    else:
                        points += result[frame+2][0]
                elif result[frame+1][1] == '/':
                    points += 10
                else:
                    points += result[frame+1][0] + result[frame+1][1]

            elif result[frame][1] == '/':
                points += 10
                if result[frame+1][0] == 'X':
                    points += 10
                else:
                    points += result[frame+1][0]

            else:
                points += result[frame][0] + result[frame][1]

        except IndexError:
            if result[frame + 1][1] == 'X':
                points += 10
            else:
                points += result[frame + 1][1]

        point_list.append(points)

    for throw in range(len(last_frame)):
        if last_frame[throw] == 'X':
            points += 10
        if last_frame[throw] == '/':
            points += 10
            points -= last_frame[throw-1]
        if isinstance(last_frame[throw], int):
            points += last_frame[throw]

    point_list.append(points)
    print(point_list)
    return point_list


player_one_gamebar = tk.Frame(main_page)
player_one_gamebar.pack()
smallFrameTemplate = tk.Frame(player_one_gamebar)
smallFrameTemplate.pack()


tk.mainloop()


calculate_points([['X'],[9,'/'],[5,'/'],[7,2],['X'],['X'],['X'],[9,0],[8,'/'],[9,'/','X']])
calculate_points([[1,4],[4,5],[6,'/'],[5,'/'],['X'],[0,1],[7,'/'],[6,'/'],['X'],[2,'/',6]])
calculate_points([['X'],['X'],['X'],['X'],['X'],['X'],['X'],['X'],['X'],['X','X','X']])