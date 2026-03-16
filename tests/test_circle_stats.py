from circle_stats import has_intersection, radius_sum

# TEST 1 – bezny pripad (2 prieniky)
def test_two_intersections():

    circle_1 = {"x": 0, "y": 0, "r": 3}
    circle_2 = {"x": 4, "y": 0, "r": 3}

    result = has_intersection(circle_1, circle_2)

    assert result == {"is_intersection": True, "intersections_count": 2}


# TEST 2 – bez prieniku
def test_no_intersection():

    circle_1 = {"x": 0, "y": 0, "r": 2}
    circle_2 = {"x": 10, "y": 0, "r": 2}

    result = has_intersection(circle_1, circle_2)

    assert result == {"is_intersection": False, "intersections_count": 0}


# TEST 3 – dotyk zvonku
def test_touching_outside():

    circle_1 = {"x": 0, "y": 0, "r": 2}
    circle_2 = {"x": 4, "y": 0, "r": 2}

    result = has_intersection(circle_1, circle_2)

    assert result == {"is_intersection": True, "intersections_count": 1}


# TEST 4 – dotyk zvnútra
def test_touching_inside():

    circle_1 = {"x": 0, "y": 0, "r": 5}
    circle_2 = {"x": 3, "y": 0, "r": 2}

    result = has_intersection(circle_1, circle_2)

    assert result == {"is_intersection": True, "intersections_count": 1}


# TEST 5 – negativny test (jedna kruznica vo vnutri druhej)
def test_one_inside_other():

    circle_1 = {"x": 0, "y": 0, "r": 5}
    circle_2 = {"x": 1, "y": 1, "r": 1}

    result = has_intersection(circle_1, circle_2)

    assert result == {"is_intersection": False, "intersections_count": 0}


# TEST 6 – test radius_sum
def test_radius_sum():

    result = radius_sum(3,4)

    assert result == 7