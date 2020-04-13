#version 330

layout(location = 0) in vec3 in_position;
layout(location = 1) in vec3 in_color;
layout(location = 2) in vec3 in_normal;

uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;

out vec3 fragment_color;
out vec3 fragment_position;
out vec3 normal;

void main()
{
    gl_Position = projectionMatrix * viewMatrix * modelMatrix * vec4(in_position, 1.0f);

    fragment_color = in_color;
    fragment_position = vec3(modelMatrix * vec4(in_position, 1.0f));
    normal = in_normal;
}
