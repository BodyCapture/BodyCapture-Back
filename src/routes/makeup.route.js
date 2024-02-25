import {makeupController} from './controllers/makeup.controller.js';
// makeupRoutes.js
const express = require('express');
const MakeupController = require('../controllers/makeup.controller');

const router = express.Router();

const makeupController = new MakeupController(); // 올바른 클래스 생성 방법

router.get('/makeup', makeupController.getAllMakeup);

module.exports = router;
