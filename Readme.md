В папке selenium нет geckodriver и selenium-server 
Ссылка на geckofriver: https://github.com/mozilla/geckodriver/releases 
Ссылка на selenium-server: http://selenium-release.storage.googleapis.com/index.html?path=3.0/


Функции для тестирования всяих штук
done - сделан
<br/>
? - невыполнимо
<br/>
1. Проверить возможность удалить запись из своей ленты - done?
<br/>
`delete_own_post`
<br/>
2. Проверить появление собственной записи в собственной ленте - done
<br/>
`create_post`
<br/>
3. Проверить возможность появления собственной публикации в чужой ленте - ???
<br/>
4. Проверить возможность появления публикации сообщества в своей ленте - ???
<br/>
5. Проверить возможность перейти по ссылке на запись из ленты - done
<br/>
`getPost`
<br/>
6. Проверить возможность по ссылке на автора записи из ленты - done
<br/>
`*getAuthorz`
<br/>
7. Проверить возможность поставить лайк собственной записи - done
<br/>
`*makeLikeOnOwnPost`
<br/>
8. Проверить возможность оставить комментарий под собственной записью - done
<br/>
`*makeSelfComment`
<br/>
9. Проверить возможность оставить комментарий под записью в ленте - done
<br/>
`*makeComment`
<br/>
10. Проверить возможность поставить лайк собственному комментарию - done
 <br/>
`*makeLikeOnSelfComment`
<br/>
11. Проверить возможность поставить лайк чужой записи - TODO
<br/>
`*makeLike`
<br/>
12. Проверить возможность оставить комментарий под записью сообщества - done (надо дофиксить)
 <br/>
`*makeGroupComment`
<br/>
13. Проверить возможность поставить лайк чужому комментарию - done
<br/>
`*makeLikeForSomemoneComment`
<br/>
14. Проверить возможность поставить несколько лайков одному комментарию - done
<br/>
`*Выше`
<br/>
15. Проверить возможность поставить несколько лайков одной записи в ленте - TODO
<br/>
`*Выше`
<br/>
16. Проверить возможность репоста фотографии - done
<br/>
`*repostPhoto`
<br/>
17. Проверить возможность репоста видео - done
<br/>
`*repostVideo`
<br/>
18. Проверить возможность репоста записи сообщества - done
<br/>
`*makeRepost`
<br/>
19. Проверить возможность репоста записи из чужой ленты - done
<br/>
`*makeRepost`
<br/>
20. Проверить возможность повторого репоста одного и того же контента - done
<br/>
`*makeRepost`
<br/>
21. Проверить двойное нажатие по кнопке репоста - done
<br/>
`*repostDoubleClick`
<br/>
22. Проверить возможность удаления репоста - done
<br/>
`*delete_repost`
<br/>
23. Проверить поведение счетчика репостов при добавлении репоста - ?
<br/>
