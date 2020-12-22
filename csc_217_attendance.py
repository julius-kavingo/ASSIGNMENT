def csc_217_attendance():
    listing_1 = open('CSC_217_attendance_ week1_30.txt', 'r').readlines()
    listing_2 = open('CSC_217_attendance_ week1_end.txt', 'r').readlines()
    listing_1 += listing_2
    new_listing = set(listing_1)
    listing_3 = open('csc_attendance.txt', 'w')
    for items in new_listing:
        listing_3.writelines(items)


csc_217_attendance()


