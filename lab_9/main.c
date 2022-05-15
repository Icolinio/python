//
//  main.c
//  lab_9
//
//  Created by Nicolas Bienek on 13/05/2022.
//

#include <stdio.h>
#include "linesegment.h"

int main(int argc, const char * argv[]) {
    LineSegment odc1 = makeLineSegment(2,3,4,5);
    show(&odc1);
    lenght(&odc1);
    printf("%f \n", lenght(&odc1));
    return 0;
}
