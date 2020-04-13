#version 120

varying vec3 light_color;

void main()
{
    gl_FragColor = vec4(light_color * fragment_color, 1.0);
}
