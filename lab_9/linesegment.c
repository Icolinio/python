//
//  linesegment.c
//  lab_9
//
//  Created by Nicolas Bienek on 13/05/2022.
//

#include "linesegment.h"
#include <stdio.h>
#include <math.h>

LineSegment makeLineSegment(int ax, int ay, int bx, int by){
    LineSegment temp;
    temp.a.x = ax;
    temp.a.y = ay;
    temp.b.x = bx;
    temp.b.y = by;
    return temp;
}
void show(const LineSegment *s){
    printf("Poczatek odcinka: (%d, %d)\n", s->a.x, s->a.y);
    printf("Koniec odcinka: (%d, %d)\n", s->b.x, s->b.y);

}
double lenght(const LineSegment *s){
    float ax = s -> a.x, ay = s -> a.y, bx = s -> b.x, by = s -> b.y;
    double len;
    len = sqrt(pow(bx - ax, 2) + pow(by - ay, 2));
    return len;
}
bool parallel(const LineSegment *s1, const LineSegment *s2){
    float ax = s1 -> a.x, ay = s1 -> a.y, bx = s1 -> b.x, by = s1 -> b.y;
    float cx = s2 -> a.x, cy = s2 -> a.y, dx = s2 -> b.x, dy = s2 -> b.y;
    kierunkowy1 = (by - bx) / (ay - ax)
}
