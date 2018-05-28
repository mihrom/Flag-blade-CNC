from mymath import *


def get_pos_not_number_char(line, start):
    i = start
    num_chars = '.+-0123456789'
    while i < len(line) and (line[i] in num_chars):
        if line[i] == '.':
            num_chars = '+-0123456789'
        i = i + 1
    return i


def extract_num_by_mark(line, marker, def_value):
    marker_pos = line.lower().find(marker)
    if marker_pos == -1:
        return line, def_value
    end_num = get_pos_not_number_char(line, marker_pos + len(marker))
    if end_num == marker_pos + len(marker):
        return line[:marker_pos + len(marker):] + line[end_num::], def_value
    return line[:marker_pos + len(marker):] + line[end_num::], float(line[marker_pos + len(marker):end_num:])


def extract_xy_from_line(line, def_x_value, def_y_value):
    line, x_value = extract_num_by_mark(line, 'x', def_x_value)
    line, y_value = extract_num_by_mark(line, 'y', def_y_value)
    return line, x_value, y_value


def extract_xyz_from_line(line, def_x_value, def_y_value, def_z_value):
    line, x_value = extract_num_by_mark(line, 'x', def_x_value)
    line, y_value = extract_num_by_mark(line, 'y', def_y_value)
    line, z_value = extract_num_by_mark(line, 'z', def_z_value)
    return line, x_value, y_value, z_value


def read_nc_file(fname, operegenie, debug=0, colangel=0.15, colline=3):
    blade_pre = Vect(0, 0)
    shpendel_pre = Vect(0, 0)
    delta = Vect(0, 1)
    delta_pre = Vect(0, 0)

    x, y, z = 0, 0, 0
    lines = []

    f = open(fname)
    for line in f:
        gline, x, y, z = extract_xyz_from_line(line, x, y, z)
        blade = Vect(x, y)

        if z >= 0 or abs(blade - blade_pre) < 0.001:
            shpendel = blade + delta * operegenie
            lines.append([line, gline, x, y, z, shpendel, 'yellow'])
        else:
            delta = blade - blade_pre
            hypot = abs(delta)
            delta = delta.norm()

            alfa = delta.get_angel_r(delta_pre)
            if abs(delta - delta_pre.rotate(alfa)) > 0.0001:
                alfa = -alfa

            shpendel = blade + delta * operegenie
            if abs(alfa) > colangel or abs(shpendel - shpendel_pre) > colline:
                if alfa >= 0:
                    j = colangel
                else:
                    j = -colangel
                k = j
                color = 'cyan'
                while abs(k) < abs(alfa):
                    shpendel = blade_pre + delta_pre.rotate(k) * operegenie
                    lines.append([line, gline, x, y, z, shpendel, color])
                    k += j
                    if color == 'cyan':
                        color = 'violet'
                    else:
                        color = 'cyan'
                shpendel = blade_pre + delta * operegenie
                lines.append([line, gline, x, y, z, shpendel, 'lime'])

            if hypot != 0:
                shpendel = blade + delta * operegenie
                lines.append([line, gline, x, y, z, shpendel, 'blue'])

        if debug:
            print('x=' + str(x) + ' y=' + str(y) + ' z=' + str(z) + '  --  ' + line.rstrip('\n'))

        blade_pre = blade
        shpendel_pre = shpendel
        delta_pre = delta
    return lines


def write_nc_file(fname, lines, debug=0):
    my_file = open(fname, "w")
    for line in lines:
        if line[1].lower().find('z') != -1:
            line[1] = line[1].lower().replace('z', 'Z' + str(line[4]))
        line[1] = line[1].replace('X', '{}').replace('x', '{}').replace('Y', '{}').replace('y', '{}')
        line[1] = line[1].format('X' + str(line[5].x) + 'Y' + str(line[5].y), '')
        if debug:
            print(line)
        my_file.write(line[1])
    my_file.close()


def get_nc_window(lines):
    minx, miny, maxx, maxy = 0, 0, 0, 0
    for line in lines:
        x = float(line[2])
        y = float(line[3])
        if x < minx: minx = x
        if x > maxx: maxx = x
        if y < miny: miny = y
        if y > maxy: maxy = y
    return minx, miny, maxx, maxy
