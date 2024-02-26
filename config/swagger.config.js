import SwaggerJsdoc from 'swagger-jsdoc';

const options = {
    definition: {
        info: {
            title: 'bodycapture',
            version: '0.0.1',
            description: 'bodycapture',
        },
        host: 'localhost:3000',
        basepath: '../',
    },
    apis: ['./routes/*.js', './swagger/*'],
};

export const specs = SwaggerJsdoc(options);