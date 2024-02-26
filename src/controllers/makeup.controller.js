import { response } from "../../config/response.js";
import { status } from "../../config/response.status.js";

import { getAllMakeup } from "../services/makeup.service.js";

export async function getAllMakeupController(req, res) {
  try {
    const makeupList = await getAllMakeup(); // 이 부분 수정
    res.json(makeupList);
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
}