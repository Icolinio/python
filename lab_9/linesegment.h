//
//  linesegment.h
//  lab_9
//
//  Created by Nicolas Bienek on 13/05/2022.
//


#ifndef linesegment_h
#define linesegment_h
#include "point.h"
#include <stdio.h>
#include <stdbool.h>

typedef struct LineSegment{
    Point a;
    Point b;
} LineSegment;
LineSegment makeLineSegment(int ax, int ay, int bx, int by);
LineSegment makeLineSegmentFromPoints(const Point *a,const Point *b);
void show(const LineSegment *s);
double lenght(const LineSegment *s);
bool parallel(const LineSegment *s1, const LineSegment *s2);

#endif /* linesegment_h */
