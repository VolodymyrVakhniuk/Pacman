#version 330

layout(location = 0) in vec3 in_position;
layout(location = 1) in vec3 in_color;

uniform float offsetsX[400];
uniform float offsetsY[400];

uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;

out vec3 fragment_color;

void main()
{
    float offsetX = offsetsX[gl_InstanceID];
    float offsetY = offsetsY[gl_InstanceID];
    vec3 position = vec3(in_position.x + offsetX, in_position.y, in_position.z + offsetY);
    
    gl_Position = projectionMatrix * viewMatrix * modelMatrix * vec4(position, 1.0f);
    fragment_color = in_color;
}
