import tkinter as tk

players = 2
plays = 10

main_page = tk.Tk()
main_page.title("BowlingAlley")
main_frame = tk.Frame(main_page)
main_frame.pack()


def numv(char):
    try:
        return int(char)
    except ValueError:
        return char


def calculate_points(result: list) -> list:
    points = 0
    point_list = []
    last_frame = result[len(result) - 1]

    for frame in range(len(result) - 1):
        try:
            if result[frame][0] == 'X':
                points += 10
                if result[frame + 1][0] == 'X':
                    points += 10
                    if result[frame + 2][0] == 'X':
                        points += 10
                    else:
                        points += result[frame + 2][0]
                elif result[frame + 1][1] == '/':
                    points += 10
                else:
                    points += result[frame + 1][0] + result[frame + 1][1]

            elif result[frame][1] == '/':
                points += 10
                if result[frame + 1][0] == 'X':
                    points += 10
                else:
                    points += result[frame + 1][0]

            else:
                points += result[frame][0] + result[frame][1]

        except IndexError:
            if result[frame + 1][1] == 'X':
                points += 10
            else:
                points += result[frame + 1][1]
        except TypeError:
            for _ in range(len(result)):
                try:
                    point_list.append(point_list[-1])
                except IndexError:
                    point_list.append(0)
            return point_list

        point_list.append(points)

    for throw in range(len(last_frame)):
        if last_frame[throw] == 'X':
            points += 10
        if last_frame[throw] == '/':
            points += 10
            points -= last_frame[throw - 1]
        if isinstance(last_frame[throw], int):
            points += last_frame[throw]

    point_list.append(points)
    return point_list


def get_and_show(mainframe: tk.Frame):
    playerlist = mainframe.winfo_children()
    playerlist.pop()
    for player in playerlist:
        result = []
        frames = player.winfo_children()
        frames.pop(0)
        for frame in frames:
            throws = frame.winfo_children()
            throws.pop()
            throw0 = throws[0].get()
            throw1 = throws[1].get()
            if throw0 == ('X' or 'x') or throw1 == ('X' or 'x'):
                frame_result = ['X']
            else:
                frame_result = [numv(throw0), numv(throw1)]
            if len(throws) == 3:
                throw2 = throws[2].get()
                frame_result = [numv(throw0), numv(throw1), numv(throw2)]
            result.append(frame_result)
        points = calculate_points(result)
        for i, frame in enumerate(frames):
            scores = frame.winfo_children()
            scores = scores.pop()
            scores.config(text=str(points[i]))


def create_players(player_count: int, frames_count: int, mainframe: tk.Frame):
    for q in range(player_count):
        gamebar = tk.Frame(mainframe)
        gmb_label = tk.Label(gamebar, text="Player " + str(q + 1))
        gmb_label.grid(row=0, column=0, padx=5, pady=5)
        for i in range(frames_count):
            small_frame_template = tk.Frame(gamebar, background='BLACK', borderwidth=1)
            throw_one_entry = tk.Entry(small_frame_template, width=1)
            throw_one_entry.grid(row=0, column=0, padx=5, pady=5)
            throw_two_entry = tk.Entry(small_frame_template, width=1)
            throw_two_entry.grid(row=0, column=1, padx=5, pady=5)
            if i == frames_count - 1:
                throw_three_entry = tk.Entry(small_frame_template, width=1)
                throw_three_entry.grid(row=0, column=2, padx=5, pady=5)
                point_label = tk.Label(small_frame_template)
                point_label.grid(row=1, column=0, columnspan=3, padx=5, pady=5)
            else:
                point_label = tk.Label(small_frame_template)
                point_label.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
            small_frame_template.grid(row=0, column=i + 1, padx=5, pady=5)
        gamebar.grid(row=q, column=0, padx=5, pady=5)


create_players(players, plays, main_frame)
calculate_button = tk.Button(main_frame, text="Calculate points", command=lambda: get_and_show(main_frame))
calculate_button.grid(row=0, column=1, padx=5, pady=5)
tk.mainloop()
