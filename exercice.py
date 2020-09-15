#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math

def square_root(a: float) -> float:
    sqr = a**(1/2)
    return sqr


def square(a: float) -> float:
    squ = a**2
    return squ


def average(a: float, b: float, c: float) -> float:
    ave = (a+b+c)/3
    return ave


def to_radians(angle_degs: float, angle_mins: float, angle_secs: float) -> float:
    degdec = angle_degs+(angle_mins+(angle_secs/60))/60
    rad = degdec*(math.pi/180)
    return rad


def to_degrees(angle_rads: float) -> tuple:
    degf = (180/math.pi)*angle_rads
    deg = int((180/math.pi)*angle_rads)
    minf = (degf-deg)*60
    min = int((degf-deg)*60)
    sec = (minf-min)*60
    return deg, min, sec


def to_celsius(temperature: float) -> float:
    cels = (temperature-32)*(5/9)
    return cels


def to_farenheit(temperature: float) -> float:
    faren = temperature*(9/5)+32
    return faren


def main() -> None:
    print(f"La racine carré de 144 est : {square_root(144)}")

    print(f"Le carré de 12 est : {square(12)}")

    print(f"Moyenne des nombres 2, 4, 6: {average(2, 4, 6)}")

    print(f"Conversion de 100 degres, 2 minutes et 45 secondes en radians: {to_radians(180, 2, 45)}")
    
    degrees, minutes, seconds = to_degrees(1.0)
    print(f"Conversion de 1 radian en degres: {degrees} degres, {minutes} minutes et {seconds} secondes")

    print(f"Conversion de 100 Celsius en Farenheit: {to_farenheit(100.0)}")
    print(f"Conversion de 451 Farenheit en Celsius: {to_celsius(451.0)}")


if __name__ == '__main__':
    main()
