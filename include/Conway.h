#include <ncurses.h>  
#include <stdlib.h>  
extern int width;
extern int height;
extern int **cell;



void init_cells(int  _w, int  _h);
void draw_cells(int  _w, int  _h);
int count_neighbors(int  _w, int  _h,int x, int y)  ;
void update_cells(int  _w, int  _h) ;
void load_pattern(int _x, int _y, char *rle_file);
void snap_shoot(char *bmp_file);
void free_cells();
void set_rand_cells();



