#include "include/createBMP.h"




void createBMPHeader(struct BMPHeader *_header,
                     int _width,
                     int _height,
                     int _pixel_size,
                     int _padding)
{
    _header->type = 0x4D42;
    _header->size = sizeof(struct BMPHeader) + (_width * _pixel_size + _padding) * _height;
    _header->offset = sizeof(struct BMPHeader);
    _header->header_size = 40;
    _header->width = _width;
    _header->height = _height;
    _header->planes = 1;
    _header->bits_per_pixel = 24;
    _header->compression = 0;
    _header->image_size = (_width * _pixel_size + _padding) * _height;
    _header->x_pixels_per_meter = 0;
    _header->y_pixels_per_meter = 0;
    _header->colors_used = 0;
    _header->important_colors = 0;
}
