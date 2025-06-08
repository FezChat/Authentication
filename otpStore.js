// otpStore.js
const store = new Map();

function saveOTP(phone, otp) {
  store.set(phone, otp);
}

function verifyOTP(phone, otp) {
  return store.get(phone) === otp;
}

function deleteOTP(phone) {
  store.delete(phone);
}

module.exports = { saveOTP, verifyOTP, deleteOTP };
