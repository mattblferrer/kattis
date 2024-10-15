def problemA() -> None:
    n = int(input())
    cubes = []
    cylinders = []

    # get input cubes, cylinders
    for _ in range(n):
        shape, size = input().split(' ')
        if shape == "cylinder":
            cylinders.append(int(size))
        else:
            cubes.append(int(size))

    # two pointers (1 for cubes, 1 for cylinders)
    cubes.sort(reverse=True)
    cylinders.sort(reverse=True)
    tower = []
    cube_ptr = 0
    cylinder_ptr = 0

    # construct tower in greedy way (biggest at the bottom)
    while cube_ptr < len(cubes) and cylinder_ptr < len(cylinders):
        # always choose biggest block size that fits
        curr_cube = cubes[cube_ptr]
        curr_cylinder = cylinders[cylinder_ptr]

        if curr_cube < curr_cylinder * (2 ** 0.5):
            tower.append(("cylinder", curr_cylinder))
            cylinder_ptr += 1
        else:
            tower.append(("cube", curr_cube))
            cube_ptr += 1

    if cube_ptr < len(cubes):
        for i in range(cube_ptr, len(cubes)):
            tower.append(("cube", cubes[i]))
    elif cylinder_ptr < len(cylinders):
        for i in range(cylinder_ptr, len(cylinders)):
            tower.append(("cylinder", cylinders[i]))

    # check if tower built is valid
    for (shape1, size1), (shape2, size2) in zip(tower, tower[1:]):
        if shape1 == "cube" and shape2 == "cylinder":
            if size1 < size2 * 2:
                print("impossible")
                return
        elif shape1 == "cylinder" and shape2 == "cube":
            if size1 < size2 / (2 ** 0.5):
                print("impossible")
                return 

    # print tower list
    for shape, size in reversed(tower):
        print(shape, size)

problemA()
