

#ifdef _BMP_CREATE_CRAZYFISH_
//DO NOTHING.
#else
#define _BMP_CREATE_CRAZYFISH_

#include <stdint.h>

// 保证结构体紧密排列
#pragma pack(push, 1)

extern const int digits[][5][3];

/**
 * @brief BMP 文件头
 *
 */
struct BMPHeader
{
    uint16_t type;               /**< 文件类型，固定为0x4D42 */
    uint32_t size;               /**< 文件大小 */
    uint16_t reserved1;          /**<  保留字段 */
    uint16_t reserved2;          /**< 保留字段 */
    uint32_t offset;             /**< 数据偏移量 */
    uint32_t header_size;        /**< 信息头大小 */
    uint32_t width;              /**< 图像宽度 */
    uint32_t height;             /**< 图像高度 */
    uint16_t planes;             /**< 色彩平面数，固定为1 */
    uint16_t bits_per_pixel;     /**< 每个像素的位数 */
    uint32_t compression;        /**< 压缩方式 */
    uint32_t image_size;         /**< 图像大小 */
    uint32_t x_pixels_per_meter; /**< 水平分辨率 */
    uint32_t y_pixels_per_meter; /**< 垂直分辨率 */
    uint32_t colors_used;        /**< 使用的颜色数 */
    uint32_t important_colors;   /**< 重要的颜色数 */
};
#pragma pack(pop)

/**
 * @brief 设置数字的颜色
 *
 * @param _color 颜色数组
 * @param _num 数字
 * @param _cx x坐标
 * @param _cy y坐标
 * @param _pwidth 笔画宽度
 */
void set_digit_color(
    unsigned char *_color, 
    int _num,              
    int _cx,               
    int _cy,               
    int _pwidth);         

/**
 * @brief 设置数字在图片中的位置
 *
 * @param _color 颜色数组
 * @param _num 数字
 * @param _x x坐标
 * @param _y y坐标
 * @param _pos_x 字符起始位置 x
 * @param _pos_y 字符起始位置 y
 * @param _width 字符宽度
 * @param _height 字符高度
 * @param _pwidth 笔画宽度
 */
void set_digit_postion(
    unsigned char *_color, 
    int _num,              
    int _x,                
    int _y,                
    int _pos_x,            
    int _pos_y,            
    int _width,            
    int _height,           
    int _pwidth);          

/**
 * @brief 创建BMP文件头
 *
 * @param _header BMP文件头
 * @param _width 图像宽度
 * @param _height 图像高度
 * @param _pixel_size 每个像素的字节数
 * @param _padding 每行的字节数需要是4的倍数
 */
void createBMPHeader(
    struct BMPHeader *_header,
    int _width,
    int _height,
    int _bits_per_pixel,
    int _padding);

#endif
