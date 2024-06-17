{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Truss Solver Function"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "def truss_solver(points, contact_patch, b):\n",
    "    arr_coeff = []\n",
    "    for key, val in points.items():\n",
    "        adj_f = val[\"f\"] - contact_patch\n",
    "        adj_i = val[\"i\"] - contact_patch\n",
    "        dist_vec = adj_f - adj_i\n",
    "        points[key][\"u\"] = dist_vec / (dist_vec[0]**2 + dist_vec[1]**2 + dist_vec[2]**2)**0.5\n",
    "        arr_coeff.append([*points[key][\"u\"], *np.cross(adj_i, points[key][\"u\"])])\n",
    "    arr_coeff = np.array(arr_coeff).T\n",
    "\n",
    "    tube_forces = np.linalg.solve(arr_coeff, b)\n",
    "    return tube_forces"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Define Suspension Geometry"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "front_contact_patch = np.array([0, 24.939, 0])\n",
    "\n",
    "front_points = {\"1\": {\"i\": np.array([-0.0629, 22.9, 11.55]), \"f\": np.array([4.426, 10, 8.45])},\n",
    "        \"2\": {\"i\": np.array([-0.0629, 22.9, 11.55]), \"f\": np.array([-5.125, 10, 7.259])},\n",
    "        \"3\": {\"i\": np.array([0.0656, 23.396, 4.2]), \"f\": np.array([4.426, 7.75, 2.899])},\n",
    "        \"4\": {\"i\": np.array([0.0656, 23.396, 4.2]), \"f\": np.array([-5.125, 7.75, 2.9])},\n",
    "        \"5\": {\"i\": np.array([0, 21.458, 11.152]), \"f\": np.array([0, 5.42, 22.534])},\n",
    "        \"6\": {\"i\": np.array([2.53, 22.761, 6.2]), \"f\": np.array([2.53, 22.76, 6.2])} }"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Evaluate Function Given [FX, FY, FZ, MX, MY, MZ]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Positive = Compression\n",
      "\n",
      "Front Bump\n",
      "FUCA: -160.395\n",
      "RUCA: -145.854\n",
      "FLCA: -123.01\n",
      "RLCA: -106.494\n",
      "Pushrod: 610.213\n",
      "Toe/Tie: -1.322\n",
      "\n"
     ]
    }
   ],
   "source": [
    "front_bump = truss_solver(front_points, front_contact_patch, np.array([0, 0, 450, 0, 0, 0]))\n",
    "\n",
    "output_labels = [\"Front Bump\"]\n",
    "force_labels = [\"FUCA\", \"RUCA\", \"FLCA\", \"RLCA\", \"Pushrod\", \"Toe/Tie\"]\n",
    "output_forces = [front_bump]\n",
    "\n",
    "print(\"Positive = Compression\\n\")\n",
    "\n",
    "for i in range(len(output_forces)):\n",
    "    forces = output_forces[i]\n",
    "    print(f\"{output_labels[i]}\")\n",
    "    for j in range(len(force_labels)):\n",
    "        print(f\"{force_labels[j]}: {round(forces[j], 3)}\")\n",
    "    print()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.6"
  },
  "orig_nbformat": 4
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
