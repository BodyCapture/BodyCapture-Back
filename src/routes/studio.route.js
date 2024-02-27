import express from "express";


import { getAllStudioController } from '../controllers/studio.controller.js';

export const studioRouter = express.Router();
console.log(getAllStudioController); 

studioRouter.get('/studioList', getAllStudioController);
