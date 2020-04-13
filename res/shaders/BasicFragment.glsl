#version 330

in vec2 texture_coords;

uniform sampler2D image;

out vec4 out_color;

void main()
{
    out_color = texture(image, texture_coords);
}
