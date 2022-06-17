import crypto from 'crypto'

//不需额外安装,这是node.js的底层模块
export const MD5Encrypt = (pwd) => { 
    let md5 = crypto.createHash('md5');
    md5.update(pwd);
    return md5.digest('hex');//md5值只能使用一次
  }

//加入盐位的MD5，盐位加在psw后
export const MD5SaltEncrypt = (pwd,saltvalue) => { 
    let md5 = crypto.createHash('md5');
    md5.update(pwd + saltvalue);
    return md5.digest('hex');//md5值只能使用一次
}

//校验密码
export const CheckPWD = (pwd,saltvalue,MD5Value) => { 
  let md5 = crypto.createHash('md5');
  md5.update(pwd + saltvalue);
  if(MD5Value == md5.digest('hex'))
    return 1;
  else
    return 0;
}

//需要安装  npm install bcryptjs
export const getbcrypt = (pwd) => {  
    var bcrypt = require('bcryptjs');    //引入bcryptjs库
    var salt = bcrypt.genSaltSync(10);    //定义密码加密的计算强度,默认10
    var hash = bcrypt.hashSync(pwd, salt); //生成hash值
    //console.log(hash);
    return hash;
  } 

export const debcrypt = (pwd, hash) => { 
    var bcrypt = require('bcryptjs'); 
    return bcrypt.compareSync(pwd, hash);
  }     
  //bcrypt.compareSync(this.registerForm.passWord, hash)  比较密码
  //若是密码相同则返回true

  //需下载npm install --save crypto-js
import CryptoJS from 'crypto-js';

 const KEY  = 'sendaverificationtoacustomerhaha';  //密钥
 //const IV   = '1234';//初始化向量

export const AESEncrypt = (data) => { 
  let key = CryptoJS.enc.Utf8.parse(KEY);
  var encrypted = CryptoJS.AES.encrypt(data, key, {
    //iv: IV,
    mode:CryptoJS.mode.ECB,
    padding: CryptoJS.pad.Pkcs7
  });
  //console.log(encrypted.toString());
  return encrypted.toString();
}

// export const AESDecrypt = (data) => {
//   var key = CryptoJS.enc.Utf8.parse(KEY);
//     var decrypted = CryptoJS.AES.decrypt(data, key, {
//       //iv: iv,
//       mode: CryptoJS.mode.ECB,
//       padding: CryptoJS.pad.Pkcs7
//     });
//     console.log(CryptoJS.enc.Utf8.stringify(decrypted).toString());
//     return CryptoJS.enc.Utf8.stringify(decrypted).toString();
// }

  // module.exports = {
  //   mdCrtpto,
  //   executebcrypt
  // }