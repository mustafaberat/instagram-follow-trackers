// 1 - INFOS: https://www.instagram.com/accounts/access_tool/ 
// https://www.instagram.com/accounts/access_tool/accounts_following_you - https://www.instagram.com/accounts/access_tool/accounts_you_follow

// 2-  mustafaberatt_XXX/followers_and_following/followers.json

myFollowers = [
  
];

myFollowed = [
  
];

hayins = [];

myFollowed.forEach((flowed) => {
  if (!myFollowers.includes(flowed)) {
    hayins.push(flowed);
  }
});

console.log(hayins);
