import numpy as np
import nose.tools as n

# IMPORT STUDENTS LINEAR ALGEBRA ASSIGNMENT AS FIRST ARGUMENT HERE
import linear_algebra_assignment_SOLN as problems


def test_one():
    result = problems.one()
    n.assert_equal(result.shape, (1,100) )


def test_two():
    result = problems.two()
    n.assert_equal(result.shape, (100,1))


def test_three():
    result = problems.three()
    n.assert_equal(result.shape, (6,6))


def test_four():
    result = problems.four()
    n.assert_equal(result.shape, (2,3))


def test_five():
    answer = np.identity(6)
    result = problems.five()
    n.assert_equal(result.all(), answer.all())


def test_six():
    answer = np.arange(0,100,1).reshape(10,10)
    result = problems.six()
    n.assert_equal(result.all(), answer.all())


def test_seven():
    M = np.arange(0,100,1).reshape(10,10)
    result = problems.seven()
    answer = M[:,:3]
    n.assert_equal(result.all(), answer.all())


def test_eight():
    M = np.arange(0,100,1).reshape(10,10)
    result = problems.eight()
    answer = M[-2:]
    n.assert_equal(result.all(), answer.all())


def test_nine():
    answer = np.arange(0,10,1).reshape(1, 10)
    result = problems.nine()
    n.assert_equal(answer.all(), result.all())


def test_ten():
    V =  np.arange(0,10,1).reshape(1, 10)
    answer = V + [0.5]
    result = problems.ten(V)
    n.assert_equal(result.all() , answer.all())


def test_eleven():
    V =  np.arange(0,10,1).reshape(1, 10)
    answer = V * [-2]
    result = problems.eleven(V)
    n.assert_equal(result.all() , answer.all())


def test_twelve():
    V =  np.arange(0,10,1).reshape(1, 10)
    B = np.zeros(10)
    B.fill(0.5)
    B.reshape(10,1)
    answer = V + B
    result_B, result_answer = problems.twelve(V)
    n.assert_equal(result_B.all() , result_answer.all())


def test_thirteen():
    answer_col = np.random.randint(10, size=(3, 1))
    answer_row = np.random.randint(10, size=(1, 3))
    answer_sq = np.random.randint(10, size=(3, 3))
    col, row, sq = problems.thirteen()
    n.assert_equal(col.shape, answer_col.shape)
    n.assert_equal(row.shape, answer_row.shape)
    n.assert_equal(sq.shape, answer_sq.shape)


def test_fourteen():
    answer_col = np.random.randint(10, size=(3, 1))
    answer_row = np.random.randint(10, size=(1, 3))
    answer_answer = answer_col * answer_row

    result = problems.fourteen(answer_col, answer_row)
    n.assert_equal( result.all(), answer_answer.all() )

def test_fifteen():
    c = np.random.randint(10, size=(3, 1))
    r = np.random.randint(10, size=(1, 3))
    s = np.random.randint(10, size=(3, 3))
    c_answer = s.dot(c)
    r_answer = r.dot(s)
    c_result, r_result = problems.fifteen(c, r, s)
    n.assert_equal(c_result.all(), c_answer.all() )
    n.assert_equal(r_result.all(), r_answer.all() )



def test_sixteen():
    c = np.random.randint(10, size=(3, 1))
    r = np.random.randint(10, size=(1, 3))
    answer = r.dot(c)
    result = problems.sixteen(c,r)
    n.assert_equal(result.all(), answer.all() )

def test_seventeen():
    a1 = False
    a2 = None
    a3 = True
    a4 = (4, 2)
    r1, r2, r3, r4 = problems.seventeen()
    n.assert_equal([r1, r2, r3, r4], [a1,a2,a3,a4])


def test_eighteen():
    a1 = np.random.randint(10, size=(3,6))
    a2 = np.reshape(a1 , (6,3))
    a3 = np.dot( a1, a2 )
    r1, r2, r3 = problems.eighteen()
    n.assert_equal([r1.shape, r2.shape, r3.shape], [a1.shape, a2.shape, a3.shape])


def test_nineteen():
    A = np.random.rand(6,2)
    B = np.random.rand(6,2)
    answer_square = np.square(A)
    answer_add  = A + B
    answer_subtract = A - B
    answer_multiply = A * B
    answer_divide =  A / B
    
    rsq, radd, rsub, rmult, rdiv = problems.nineteen()
    n.assert_equal([rsq.shape, radd.shape, rsub.shape, rmult.shape, rdiv.shape], [answer_square.shape, answer_add.shape, answer_subtract.shape, answer_multiply.shape, answer_divide.shape])


def test_twenty():
    A = np.arange(0,4).reshape(4,1)
    B = np.arange(0,3).reshape(1,3)
    answer = A + B
    result = problems.twenty()
    n.assert_equal(result.all(), answer.all() )

def test_twenty_one():
    answer = np.linspace(1, 100, 100).reshape(10,10)
    result = problems.twenty_one()
    n.assert_equal(result.all() , answer.all() )



def test_twenty_two():
    M = np.linspace(1, 100, 100).reshape(10,10)
    answer_sum, answer_mean, answer_std = M.sum(), M.mean(), M.std()
    result_sum, result_mean, result_std = problems.twenty_two(M)

    n.assert_equal( result_sum.all(), answer_sum.all() )
    n.assert_equal( result_mean.all(), answer_mean.all() )
    n.assert_equal( result_std.all(), answer_std.all() )



def test_twenty_three():
    M = np.linspace(1, 100, 100).reshape(10,10)
    answer_sum, answer_mean, answer_std = M.sum(axis=0), M.mean(axis=0), M.std(axis=0)
    result_sum, result_mean, result_std = problems.twenty_three(M)
    
    n.assert_equal( result_sum.all(), answer_sum.all() )
    n.assert_equal( result_mean.all(), answer_mean.all() )
    n.assert_equal( result_std.all(), answer_std.all() )



def test_twenty_four():
    M = np.linspace(1, 100, 100).reshape(10,10)
    answer_sum, answer_mean, answer_std = M.sum(axis=1), M.mean(axis=1), M.std(axis=1)
    result_sum, result_mean, result_std = problems.twenty_three(M)
    
    n.assert_equal( result_sum.all(), answer_sum.all() )
    n.assert_equal( result_mean.all(), answer_mean.all() )
    n.assert_equal( result_std.all(), answer_std.all() )