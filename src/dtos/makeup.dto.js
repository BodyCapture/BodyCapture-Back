// dto/MakeupDTO.js
class MakeupDTO {
    constructor(makeupId, category, district, city, makeupName, address, tel, img) {
      this.makeupId = makeupId;
      this.category = category;
      this.district = district;
      this.city = city;
      this.makeupName = makeupName;
      this.address = address;
      this.tel = tel;
      this.img = img;
    }
  }
  
  module.exports = MakeupDTO;
  