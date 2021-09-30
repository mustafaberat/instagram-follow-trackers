// INFOS: https://www.instagram.com/accounts/access_tool/

// https://www.instagram.com/accounts/access_tool/accounts_following_you
myFollowers = [
  
];

// https://www.instagram.com/accounts/access_tool/accounts_you_follow
myFollowed = [
  
];

hayins = [];

myFollowed.forEach((flowed) => {
  if (!myFollowers.includes(flowed)) {
    hayins.push(flowed);
  }
});

console.log(hayins);
