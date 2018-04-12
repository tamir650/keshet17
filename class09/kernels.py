{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {
    "collapsed": false,
    "deletable": true,
    "editable": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[<matplotlib.lines.Line2D at 0x10da39dd0>]"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x1124b9450>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "%matplotlib inline\n",
    "import matplotlib.pyplot as plt\n",
    "import matplotlib.image as mpimg\n",
    "import numpy as np\n",
    "urban_list = list()\n",
    "beach_r_list = list()\n",
    "\n",
    "for i in range(10):\n",
    "    img = mpimg.imread('../data/beach_r' + str(i) + '.jpg')\n",
    "    beach_r_list.append([img[:,:,0].sum() / img[:,:,0].size, img[:,:,2].sum() / img[:,:,2].size])\n",
    "\n",
    "    img = mpimg.imread('../data/urban' + str(i) + '.jpg')\n",
    "    urban_list.append([img[:,:,0].sum() / img[:,:,0].size, img[:,:,2].sum() / img[:,:,2].size])\n",
    "\n",
    "average = np.mean(urban_list + beach_r_list, axis=0)\n",
    "urban_array_centered = np.array(urban_list)-average   \n",
    "beach_r_array_centered = np.array(beach_r_list)-average  \n",
    "plt.plot(beach_r_array_centered[:,0], beach_r_array_centered[:,1], 'g+')\n",
    "plt.plot(urban_array_centered[:,0], urban_array_centered[:,1], 'b_')\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {
    "collapsed": true,
    "deletable": true,
    "editable": true
   },
   "outputs": [],
   "source": [
    "from IPython import display\n",
    "import time \n",
    "\n",
    "def plot_seperating_hyperlane(w):\n",
    "    print w\n",
    "    w = w / np.linalg.norm(w)\n",
    "    t = np.arange(-60.0, 80.0, 10.0)\n",
    "    plt.plot(w[1]*t, -w[0]*t, 'k--', lw=2)\n",
    "    plt.plot(beach_r_array_centered[:,0], forest_array_centered[:,1], 'g+')\n",
    "    plt.plot(urban_array_centered[:,0], city_array_centered[:,1], 'b_')\n",
    "    plt.show()\n",
    "    display.clear_output(wait=True)\n",
    "    time.sleep(0.5)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {
    "collapsed": false,
    "deletable": true,
    "editable": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ -8.07066127, -62.17923231],\n",
       "       [  9.57897025, -10.11615489],\n",
       "       [ 21.5526573 ,  -7.02326243],\n",
       "       [ 34.90629732,  -4.53920233],\n",
       "       [ 13.06751017, -49.55440928],\n",
       "       [-28.62273046, -58.45198011],\n",
       "       [ -2.04532629,   5.43604489],\n",
       "       [-17.79339538, -24.75185693],\n",
       "       [ 13.40405881,   1.46022557],\n",
       "       [ -3.51962259,  -6.56106391],\n",
       "       [ 30.33434454,  72.86523812],\n",
       "       [  8.8414532 ,   0.53770223],\n",
       "       [-30.61520328,  30.00340465],\n",
       "       [-19.82686191,  13.44959114],\n",
       "       [-24.60917754,   6.63899301],\n",
       "       [-36.5841297 ,   3.7618837 ],\n",
       "       [ 48.0243708 ,   6.30903326],\n",
       "       [ 28.30330816,  28.82610903],\n",
       "       [ 32.37461479,  39.54460672],\n",
       "       [-68.70047691,  14.34432989]])"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x = np.row_stack((urban_array_centered, beach_r_array_centered))\n",
    "x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {
    "collapsed": false,
    "deletable": true,
    "editable": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([-1, -1, -1, -1, -1, -1, -1, -1, -1, -1,  1,  1,  1,  1,  1,  1,  1,\n",
       "        1,  1,  1])"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y = np.array([-1]*10 + [1]*10)\n",
    "y"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {
    "collapsed": false,
    "deletable": true,
    "editable": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([-0.05000942,  0.99874875])"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn import linear_model\n",
    "classifier = linear_model.LogisticRegression()\n",
    "classifier.fit(x,y)\n",
    "w = classifier.coef_[0]\n",
    "w / np.linalg.norm(w)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {
    "collapsed": false,
    "deletable": true,
    "editable": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[-0.0159122   0.31778591]\n"
     ]
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAXwAAAEACAYAAACwB81wAAAABHNCSVQICAgIfAhkiAAAAAlwSFlz\nAAALEgAACxIB0t1+/AAAGORJREFUeJzt3X2QVPWd7/H3BxEZFRhwDUYJIEkU0IoQK0gl9y69MRof\noix1g9dNGYxubrKrFRP3JkYTKowx2VXrWppksyapRK4bUj4SBbkmKhU7VipBRUTFAYIPPBuMsiAo\noMj3/nEOYzOnB5jununuOZ9X1RSnf/3rPl/O9Hz617/z0IoIzMys7+tX7wLMzKx3OPDNzHLCgW9m\nlhMOfDOznHDgm5nlhAPfzCwnahL4kq6UtEzSs5J+JWmApNGSFklaKekOSf1rsS4zM6tM1YEv6Vjg\nK8BHI+IjQH/gH4AbgJsi4kRgC/CP1a7LzMwqV6spnUOAI9JRfAuwEfg7YG56/+3AtBqty8zMKlB1\n4EfERuAmYC2wAdgKLAG2RMSetNt64Nhq12VmZpWrxZROKzAVGEUS6kcAZ5fp6ms4mJnVUS12pH4K\neCkiNgNIug/4ONAqqV86yh9BMs2TIclvBGZmFYgIdad/Lebw1wKTJQ2UJOB04HngUWB62udiYF5X\nTxARDf8za9asutfgOl1ns9boOmv/U4lazOE/AdwLPA08Awj4GXA18C+S/gwMA35R7brMzKxyNTk2\nPiKuBa7t1PwycFotnt/MzKrnM20PUqFQqHcJB8V11lYz1NkMNYLrbASqdC6oZgVIUe8azMyajSSi\nDjttzcysCTjwzays4upivUuwGnPgm1lZDvy+x4FvZpYTvmSxmXUori52jOyv/f17R1oXRhcojC7U\npyirGQe+mXXoHOxthba61WK15ykdM7OccOCbWVmewul7fOKVmVkT8olXZmbWJQe+mVlOOPDNzHLC\ngW9mlhMOfDOznHDgm5nlhAPfzCwnHPhmZjlRk8CXNETSPZKWS3pe0mmShkp6WNJKSQ9JGlKLdZmZ\nWWVqNcL/AfBgRIwDTgFWAFcDCyPiROB3wDU1WpeZmVWg6ksrSBoELI2ID3ZqXwFMiYhNko4BihEx\ntszjfWkFM7NuqtelFcYAr0maLWmJpJ9JOhwYHhGbACLiL8DRNViXmZlVqBbXw+8PfBS4PCIWS7qZ\nZDrnoIftbW1tHcuFQoFCoVCDsszM+o5isUixWKzqOWoxpTMc+FNEjElv/zeSwP8gUCiZ0nk0nePv\n/HhP6ZiZdVNdpnTSaZt1kk5Im04HngfmA19I2y4G5lW7LjMzq1xNrocv6RTg58ChwEvAJcAhwN3A\nB4C1wPSI2FLmsR7hm5l1UyUjfH8BiplZE/IXoJiZWZcc+GZmOeHANzPLCQe+mVlOOPDNzHLCgW9m\nlhMOfDOznHDgm5nlhAPfzCwnHPhmZjnhwDczywkHvplZTjjwzcxywoFvZpYTDnwzs5xw4JuZ5YQD\n38wsJxz4ZmY54cA3M8uJmgW+pH6Slkian94eLWmRpJWS7pDUv1brMjOz7qvlCP+rQHvJ7RuAmyLi\nRGAL8I81XJeZmXVTTQJf0gjgHODnJc2fBOamy7cD02qxLjOrj+LqYr1LsCrVaoR/M/ANIAAkHQX8\nV0TsSe9fDxxbo3WZWR048Jtf1fPqks4FNkXEUkmFvc3pT6no6jna2to6lguFAoVCoauuZma5VCwW\nKRaLVT2HIrrM4YN7AulfgYuA3UALMAi4HzgTOCYi9kiaDMyKiLPLPD6qrcHMekZxdbFjZH/t769l\n1pRZABRGFyiMLtSvMEMSEdF5YL3/x9QybCVNAf53RJwv6S7g1xFxl6RbgWci4idlHuPAN2sCbcU2\n2gpt9S7DUpUEfk8eh3818C+S/gwMA37Rg+syM7MDqOkIv6ICPMI3awrF1UVP4zSQuk/pVMKBb2bW\nfY02pWNmZg3EgW9mlhMOfDOznHDgm5nlhAPfzCwnHPi2X75+ilnf4cC3/XLgm/UdDnwzA/zmngf+\nFirL6HzBrL18way+zWfS9n0OfMvoHOy+YJZZ3+DAN8sxf5rLFwe+7Zf/6Ps2f5rLF++0tf1y4Jv1\nHQ58MwP85p4HvjyymVkT8uWRzcysSw58M7OccOCbmeVE1YEvaYSk30lql/ScpCvS9qGSHpa0UtJD\nkoZUX66ZmVWq6p22ko4BjomIpZKOBJ4CpgKXAK9HxI2SvgkMjYiryzzeO23NzLqpLjttI+IvEbE0\nXd4OLAdGkIT+7Wm324G/r3ZdZmZWuZrO4UsaDUwAFgHDI2ITJG8KwNG1XJeZmXVPzS6tkE7n3At8\nNSK2SzroeZq2traO5UKhQKFQqFVZZmZ9QrFYpFgsVvUcNTnxSlJ/YAHwm4j4Qdq2HChExKZ0nv/R\niBhX5rGewzcz66Z6nnh1G9C+N+xT84EvpMsXA/NqtC4zM6tALY7S+QTwGPAcEOnPt4AngLuBDwBr\ngekRsaXM4z3CNzPrpkpG+L6WjplZE/K1dMrw93SamSUc+FYX/r2Y9b4+H/jWmBz4Zr2vT37Fob+n\n08wsq08Gvr+nszH5jdisvvpk4Ftj8huxWX31+Tl8jxzNzBIOfKsL/17Mep9PvDIza0I+8crMzLrk\nwDczywkHvtWUT6iynuTXV3Uc+FZT/oO0nuTXV3Uc+GZmOeETr6xqPoPWepJfX7XjwM+R4upij/yB\n+Axa60l+fdWOAz9Heirwm1mxmPx0VigkP2Z9iQPfaqrZ3lAc7M2lt15fb731Fjt27GDnzp3s2LGj\nY/nUU0+lX7/srs8f/ehHbN++fZ/H7Ny5kx//+McMGDCgV2o+GD7Tto/rPP85a8oswPOf1vj27NmD\nJKTsyaR//OMfywbspZdeWjZgv/jFL7Jly5ZM/z/84Q8cfvjhmf6DBg1i+/btmfatW7cyePDgTPvg\nwYPZtm1bpn3Lli0MGTLkYP/L3VLJmbY9PsKXdBZwC8kRQb+IiBt6ep32Hs9/NoZmn04rHeWW/jth\nwgT698/GyK233srWrVszo+RbbrmFI444ItP/tNNO49VXX92n/9tvv83mzZsZOnRopv+5557Lli1b\nMu3Tp0/nqKOOyrTfd999bN68OdP+1ltvlQ38oUOHcuihh9LS0sLAgQM7/n333XfLbp8rrriC3bt3\nZ/ofdthhZfvXS48GvqR+wL8DpwMbgSclzYuIFT25XrNGU4vA39+I9/HHH+eNN97IBPKMGTNoaWnJ\n9L/88ss7Ara0/8KFCxk2bFim/8iRI3nttdcy7Zs2beJ973tfpn3WrFn89a9/zbRfd911ZQN/zZo1\nbNq0KdO+Y8eOsoE/ZcoU3nzzzX3CtaWlpeybD8BPf/pTIiITyF2NvteuXVu2vSvf+973utW/Xnp6\nhD8JWBURawAk3QlMBRz4ddDMI8xG03lud+/yRz7ykbJTCkuWLOH6RddnAvnGG29k6dLWzI7j2bNn\n8/bbDwPFjr67du1i48aNvP/97888/7Rp03jllVcy7eeeey4jRozItM+bN48NGzZk2t98882ygd/a\n2sru3bszAbtnz56y2+eyyy5j586d+/QfOHAgRx55ZNn+jz32GP379+/o39LSwoABA8rOlwPcf//9\nZdu78tnPfrZb/fuqHp3Dl/Q/gE9HxJfS2xcBkyLiipI+nsO3iux93ZQb8T7xxBNs3bo1E7Cf+9zn\nGDRoUKb/1772NTZs2JAJ8gULFpQN2JEjR7Ju3bpM++rVqxk1ahRQ5vjx4t5O6Q/w8ssvM3r06Mzz\njB49mjVr1mTaX3rpJY4//vhM+wUXXMDmzZszgfz973+fo48+OtP/vvvuKxvgJ598csNNQ1h5jTiH\nX66YTLq3tbV1LBcKBQo+bKLp7Nq1q+w87/jx4xk4cGCm/+zZszNztjt37uS6664rO0Xw6U9/mhde\neGGfdezcuZMXX3yRMWPGZPpfeOGFvPzyy5n2008/vWzgL1iwgBdffDHTvm3btrKB39rayrZt2zKB\nWap0/8ljjz3GxyZ9LBm9nvVe/3LTFQALFy6kX79+mfngrka8d999d9n2rkybNq1b/a3+isUixXLH\nEHdDT4/wJwNtEXFWevtqIEp33HqEXzv7G/E+9dRTZY9SmD59Oq2trZn+V111FatXr870nzt3bscI\nttQJJ5zAqlWrMu0rVqzgxBNPzLSPHTuWlStXZtrb29sZN25cpn3cuHGsWJGdCXz++ecZP358pv2i\niy7ilVdeyczZfve73y0b4PPmzWPXrl1lR7zl3rC6q63Y5h3mVlONOMJ/EviQpFHAK8CFwD/08Dob\nQlcj3rFjx5Y9KmDOnDls3Lgx0/873/kOxx57bKb/eeedR3t7e6b/smXLOOmkkzL9Z8yYQXt7e6Z9\n8uTJZQP/N7/5DcuWLcu0b926tez/d/DgwQwePLhj/nVvYHY1Ir3kkkt4/fXXM4FcbnQP8MADDyBp\nnzne/Y1458yZU7a9K1OnTu1W/+7y/hNrBD1+HH56WOYPeO+wzOs73d8UI/yZM2eyatWqTMDOmTOn\n7Aj2lFNO4dlnn820P/3000yYMCHTPmHCBJ555plM+5IlS5g4cWKmfeLEiSxdujTTvnjxYk499dRM\n+6WXXsrq1aszgTxz5syyI/YFCxbscxTE3secdNJJZd+wzKx3NeIIn4j4LZBNxCbz0EMPsXjx4kx7\nuWOBYd8Rb+kItqvDxj7/+c9zxhlnZAL5uOOOK9v/3nvvzRxmdthhh3HIIYeU7X/bbbcd5P808ZnP\nfKZb/c2s8flM24P04IMP8sYbb+wTsC0tLYwbN67LQ83MzHpKJSN8B76ZWRNqyCkdM+t7fJXR5uQR\nvplZE/II3+wgeHRqeeURvlkf4Dex/PFOWzOznKgk8MufpmhmZn2OA9/MLCe809ash3l+3RqF5/DN\nzJqQ5/DNzKxLDnwzs5xw4JuZ5YQD38wsJxz4ZmY54cA3M8sJB76ZWU448M3McqKqwJd0o6TlkpZK\nmitpcMl910hald5/ZvWlmplZNaod4T8MnBQRE4BVwDUAksYDFwDjgLOB/5DUrTPCzMystqoK/IhY\nGBF70puLgBHp8vnAnRGxOyJWk7wZTKpmXWZmVp1azuFfCjyYLh8HrCu5b0PaZmZmdXLAq2VKegQY\nXtoEBPDtiHgg7fNt4J2IuKOkT2ddXiGtra2tY7lQKFDwJQTNzPZRLBYplrvsajdUfbVMSRcDXwI+\nGRG70rargYiIG9LbvwVmRcTjZR7vq2WamXVTr18tU9JZwFXA+XvDPjUfuFDSAEnHAx8CnqhmXWZm\nVp1qvwDlR8AA4JH0IJxFEXFZRLRLuhtoB94BLvMw3sysvvwFKGZmTchfgGJmZl1y4JuZ5YS/xNzq\nxl/ubda7PIdvZtaEPIdvZmZdcuCbmeWEA9/MLCcc+GZmOeHANzPLCQe+mVlOOPDNzHLCgW9mlhMO\nfDOznHDgm5nlhAPfzCwnHPhmZjnhwDczywkHvplZTjjwzcxyoiaBL+nrkvZIGlbS9kNJqyQtlTSh\nFusxM7PKVR34kkYAnwLWlLSdDXwwIj4MfBn4SbXrMTOz6tRihH8z8I1ObVOB/wSIiMeBIZKG12Bd\nZmZWoaoCX9J5wLqIeK7TXccB60pub0jbzMysTg74JeaSHgFKR+cCApgJfAs4o9zDyrR1+cW1bW1t\nHcuFQoGCv8HazGwfxWKRYrFY1XNU/CXmkk4GFgJvkQT8CJKR/CTgu8CjEXFX2ncFMCUiNpV5Hn+J\nuZlZN/Xql5hHxLKIOCYixkTE8cB6YGJEvArMB2akRU0GtpQLezMz6z0HnNLphiCdyomIByWdI+kF\n4E3gkhqux8zMKlDxlE7NCvCUjplZt/XqlI6ZmTUXB76ZWU448M3McsKBb2aWEw58M7OccOCbmeWE\nA9/MLCcc+GZmOVHLM23NrJuKxeSns0Ih+TGrJZ9pa2bWhHymrZmZdcmBb2aWEw58M7OccOCbmeWE\nA9/MLCcc+GZmOeHANzPLCQe+mVlOVB34kr4iaYWk5yRdX9J+jaRVkpZLOrPa9ZiZWXWqurSCpAJw\nHnByROyW9Ddp+zjgAmAcMAJYKOnDPqXWzKx+qh3h/zNwfUTsBoiI19L2qcCdEbE7IlYDq4BJVa7L\nzMyqUO3F004A/lbSvwI7gK9HxFPAccCfSvptSNusCfkCX2Z9wwEDX9IjwPDSJiCAmenjWyNisqSP\nAfcAY9I+nXk6p0k52M36hgMGfkSc0dV9kv4J+HXa70lJ70o6ClgPjCzpOgLY2NXztLW1dSwXCgUK\nThczs30Ui0WK5T5qd0NVl0eW9CXguIiYJekE4JGIGCVpPPAr4DSSqZxHgLI7bX15ZDOz7qvk8sjV\nzuHPBm6T9BywC5gBEBHtku4G2oF3gMuc6mZm9eUvQLE+xTuYLS8qGeE78M3MmpC/8crMzLrkwDcz\nywkHvplZTjjwzcxywoFvZpYTDnwzs5xw4JuZ5YQD38wsJxz4ZmY54cA3M8sJB76ZWU448M3McsKB\nb2aWEw58M7OccOCbmeWEA9/MLCcc+GZmOeHANzPLiaoCX9Ipkv4k6WlJT0j6WMl9P5S0StJSSROq\nL9XMzKpR7Qj/RmBWREwEZqW3kXQO8MGI+DDwZeAnVa6n7orlvhm7AbnO2mqGOpuhRnCdjaDawN8D\nDEmXW4EN6fL5wH8CRMTjwBBJw6tcV101y4vAddZWM9TZDDWC62wE/at8/JXAQ5JuAgR8PG0/DlhX\n0m9D2rapyvWZmVmFDhj4kh4BSkfnAgL4NvAp4KsRcb+kzwK3AWekfTqL6ss1M7NKKaLyHJa0JSJa\nO9+W9BPg0Yi4K21fAUyJiMwIX5LfCMzMKhAR5QbXXap2SmeDpCkR8XtJpwOr0vb5wOXAXZImA1vK\nhT10v2AzM6tMtYH/v4AfSjoE2Al8CSAiHpR0jqQXgDeBS6pcj5mZVamqKR0zM2sedTvTtplO2pL0\nFUkrJD0n6fqS9mvSOpdLOrOeNe4l6euS9kgaVtLWENtT0o3ptloqaa6kwSX3NdS2lHRW+jv/s6Rv\n1ruevSSNkPQ7Se3p6/GKtH2opIclrZT0kKQhB3quXqi1n6Qlkuant0dLWpTWeIekamcYakLSEEn3\npK+95yWd1mjbU9KVkpZJelbSryQNqGh7RkRdfoCHgDPT5bNJdvICnAP8v3T5NGBRvWpMaygADwP9\n09t/k/47DniaZFpsNPAC6SemOtY6Avgt8DIwrGTbNsT2JDmqq1+6fD3wb+ny+EbaliQDoReAUcCh\nwFJgbD1/tyW1HQNMSJePBFYCY4EbgKvS9m8C1zdArVcCc4D56e27gOnp8q3Al+tdY1rL/wUuSZf7\nk5xb1DDbEzgWeAkYULIdL65ke9bzWjrNctLWP5P8snenNb2Wtk8F7oyI3RGxmmSH9aT6lNjhZuAb\nndqm0iDbMyIWRsSe9OYikjcoSH7njbQtJwGrImJNRLwD3EmyHesuIv4SEUvT5e3AcpLtOBW4Pe12\nO/D39akwIWkEyeDt5yXNnwTmpsu3A9N6u67OJA0C/ntEzAZIX4NbabDtCRwCHJGO4luAjcDf0c3t\nWc/AvxL4P5LWklyS4Zq0vauTturlBOBv049Oj0o6NW1vqDolnQesi4jnOt3VUHWWuBR4MF1utBo7\n17Oexthm+5A0GphA8uY5PNIj4SLiL8DR9asMeG/wEQCSjgL+q+QNfz3JyLXexgCvSZqdTj/9TNLh\nNND2jIiNwE3AWpK/ja3AEpKjH7u1PXt0Dq1ZTtraT50zSbZRa0RMTvcz3EPyImm0Or9Fsv0yDyvT\n1mN17u93HhEPpH2+DbwTEXfUo8aD0Gj1ZEg6EriX5G9oeyOdzyLpXGBTRCyVVNjbTHa7NkLN/YGP\nApdHxGJJNwNX0xi1ASCpleQTxyiSsL+HZKq2swPW3KOBHxHlAggASb+MiK+m/e6VtPej33rgAyVd\nR5B8fOkxB6jzn4Bfp/2elPRuOlpZD4xshDolnUwy9/2MJKW1LJE0iV7envvblgCSLib5qP/JkuZe\n/50fQK//brsj/Vh/L/DLiJiXNm+SNDwiNkk6Bni1fhXyCeB8JRdRbAEGAbeQTCf2S0eljbJN15N8\nMl6c3p5LEviNtD0/BbwUEZsBJN1Hchmb1u5uz3pO6WyQNAVA2ZO2ZqTt+z1pq5fcD5ye1nMCyY6T\n10nq/J/p3vLjgQ8BT9SjwIhYFhHHRMSYiDie5EU8MSJepYG2p6SzgKuA8yNiV8ld84ELG2Fbpp4E\nPiRplKQBwIVpjY3iNqA9In5Q0jYf+EK6fDEwr/ODektEfCsiRkbEGJJt97uIuAh4FJjeCDXulf4t\nrEv/tiH5W3+eBtqeJFM5kyUNTAd0e2vs/vas457njwOLSY7O+BNJQO29799JjpJ4BvhovWpMazkU\n+CXwXFrvlJL7rknrXE56xFEj/JDs0R/WaNuT5E19Dcn84xLgPxp1WwJnkRwBswq4ut71lNT1CeBd\nkiOHnk6341nAMGBhWvMjJNOQjVDvFN47Sud44HHgzyRHmBxa7/rSuk4heZNfSvJpfkijbU+Sy88v\nB54l2UF7aCXb0ydemZnlhL/i0MwsJxz4ZmY54cA3M8sJB76ZWU448M3McsKBb2aWEw58M7OccOCb\nmeXE/wdPaLp7p5rafwAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x1128f8bd0>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plot_seperating_hyperlane(w)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {
    "collapsed": false,
    "deletable": true,
    "editable": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([-0.03015084,  0.99954536])"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn import svm\n",
    "\n",
    "classifier = svm.SVC(kernel='linear')\n",
    "classifier.fit(x,y)\n",
    "\n",
    "w = classifier.coef_[0]\n",
    "w / np.linalg.norm(w)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {
    "collapsed": false,
    "deletable": true,
    "editable": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[-0.00576887  0.19124677]\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x112812390>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plot_seperating_hyperlane(w)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true,
    "deletable": true,
    "editable": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true,
    "deletable": true,
    "editable": true
   },
   "outputs": [],
   "source": [
    "from sklearn import svm\n",
    "\n",
    "classifier = svm.SVC(kernel='linear')\n",
    "classifier.fit(x,y)\n",
    "\n",
    "w = classifier.coef_[0]\n",
    "w / np.linalg.norm(w)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true,
    "deletable": true,
    "editable": true
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 2",
   "language": "python",
   "name": "python2"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
