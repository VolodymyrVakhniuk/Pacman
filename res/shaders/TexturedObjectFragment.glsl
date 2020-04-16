#version 330

in vec2 texture_coords;

//uniform float alpha_value;
uniform sampler2D image;

out vec4 out_color;

void main()
{
    out_color = texture(image, texture_coords);//vec4(vec3(texture(image, texture_coords), alpha_value);
}
