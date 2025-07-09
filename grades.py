def grades_classify(a):
    g="A"
    if a<35:
        g="FAIL"
    elif a<50:
        g="D"
    elif a<75:
        g="C"
    elif a<=80:
        g="B"
    elif a<100:
        g="A"
    print("Grade ",g)

