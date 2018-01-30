def get_above_avg_marks(marks):
    # average marks
    # new_marks = []
    avg = sum(marks) / len(marks)
    # for m in marks:
    #     if m > avg:
    #         new_marks.append(m)
    new_marks = [m for m in marks if m > avg]
    return new_marks


marks = [50, 70, 80, 90, 44, 77]

print(get_above_avg_marks(marks))
