import express from "express";


import { getAllMakeupController } from '../controllers/makeup.controller.js';

export const makeupRouter = express.Router();
console.log(getAllMakeupController); 

makeupRouter.get('/makeup', getAllMakeupController);
