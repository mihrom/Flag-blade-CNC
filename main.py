import sys
from readgcode import *
from graph import *


def main(argv=sys.argv):
    if len(argv) > 1:
        fname = argv[1]
    else:
        fname = "1.tap"

    lines_b = read_nc_file(fname, 23.5)
    write_nc_file(fname + "_", lines_b)

    ix, iy, ax, ay = get_nc_window(lines_b)
    print(ix, iy, ax, ay)

    screen = Graph(ix, iy, ax, ay, 500, 500)
    screen.drow_curv_red(lines_b)
    screen.drow_curv_blue(lines_b)

    turtle.mainloop()
if __name__ == '__main__':
    main()
