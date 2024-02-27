import { response } from "../../config/response.js";
import { status } from "../../config/response.status.js";
//import { getAllStudio } from "../models/studio.dao.js";
//?
import { getAllStudio } from "../services/studio.service.js";

export async function getAllStudioController(req, res) {
  try {
    const studioList = await getAllStudio(); // 이 부분 수정
    res.json(studioList);
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
}