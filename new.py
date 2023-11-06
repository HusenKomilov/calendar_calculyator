year = int(input("Yilni kiritng: "))
month = int(input("Oyni kiritng: "))
day = int(input("Kunni kiritng: "))
month_all = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

if year > 1500:
    all_day = int((year - 1) * 365.25)
    if month in month_all:
        if day > 0 or day < 32:
            if year % 4 != 0:
                fev = 28
                if month == 1:
                    a = day
                elif month == 2:
                    a = day + 31
                elif month == 3:
                    a = day + fev + 31
                elif month == 4:
                    a = day + fev + 31 * 2
                elif month == 5:
                    a = day + fev + 31 * 2 + 30
                elif month == 6:
                    a = day + fev + 31 * 3 + 30
                elif month == 7:
                    a = day + fev + 31 * 3 + 30 * 2
                elif month == 8:
                    a = day + fev + 31 * 4 + 30 * 2
                elif month == 9:
                    a = day + fev + 31 * 5 + 30 * 2
                elif month == 10:
                    a = day + fev + 31 * 5 + 30 * 3
                elif month == 11:
                    a = day + fev + 31 * 6 + 30 * 3
                elif month == 12:
                    a = day + fev + 31 * 6 + 30 * 4
            elif year % 4 == 0:
                fev = 29
                if month == 1:
                    a = day
                elif month == 2:
                    a = day + 31
                elif month == 3:
                    a = day + fev + 31
                elif month == 4:
                    a = day + fev + 31 * 2
                elif month == 5:
                    a = day + fev + 31 * 2 + 30
                elif month == 6:
                    a = day + fev + 31 * 3 + 30
                elif month == 7:
                    a = day + fev + 31 * 3 + 30 * 2
                elif month == 8:
                    a = day + fev + 31 * 4 + 30 * 2
                elif month == 9:
                    a = day + fev + 31 * 5 + 30 * 2
                elif month == 10:
                    a = day + fev + 31 * 5 + 30 * 3
                elif month == 11:
                    a = day + fev + 31 * 6 + 30 * 3
                elif month == 12:
                    a = day + fev + 31 * 6 + 30 * 4
            week_num = (all_day + a) % 7
            if week_num == 1:
                week_text = "Yakshanba"
            elif week_num == 2:
                week_text = "Dushanba"
            elif week_num == 3:
                week_text = "Seshanba"
            elif week_num == 4:
                week_text = "Chorshanba"
            elif week_num == 5:
                week_text = "Payshanba"
            elif week_num == 6:
                week_text = "Juma"
            elif week_num == 0:
                week_text = "Shanba"
            print(week_text)
        else:
            print("Oydagi kunlar xato kiritgan")

