#version 120

attribute vec3 in_position;
attribute vec3 in_color;

uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;

varying vec3 fragment_color;

void main()
{
    gl_Position = projectionMatrix * viewMatrix * modelMatrix * vec4(in_position, 1.0f);
    fragment_color = in_color;
}
