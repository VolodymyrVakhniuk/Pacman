#version 330

in vec3 fragment_color;
in vec3 fragment_position;
in vec3 normal;

const int MAX_LIGHTS_NUMBER = 10;

uniform vec3 light_colors[MAX_LIGHTS_NUMBER];
uniform vec3 light_positions[MAX_LIGHTS_NUMBER];

uniform float alpha_value;

out vec4 out_color;

vec3 calculateDiffuseComponent(int lightIndex);

void main()
{
    vec3 accumulated_diffuse_componet = vec3(0.0, 0.0, 0.0);
    for(int i = 0; i < MAX_LIGHTS_NUMBER; i++)
    {
        accumulated_diffuse_componet += calculateDiffuseComponent(i);
    }
    
    vec3 resulting_color = accumulated_diffuse_componet * fragment_color;
    
    out_color = vec4(resulting_color, alpha_value);
}

vec3 calculateDiffuseComponent(int lightIndex)
{
    vec3 norm = normalize(normal);
    vec3 light_direction = normalize(fragment_position - light_positions[lightIndex]);

    float diff = max(dot(norm, light_direction), 0.0);
    vec3 diffuse = diff * light_colors[lightIndex];

    return diffuse;
}
