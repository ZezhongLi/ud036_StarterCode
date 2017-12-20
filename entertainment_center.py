import media
import fresh_tomatoes

two_smoking_barrels = media.Movie("Lock, stock and two smoking barrels",
                     "Eddy (Nick Moran) convinces three friends to pool funds for a high-stakes poker game against local crime boss Hatchet Harry (P.H. Moriarty). Harry cheats and Eddy loses, giving him a week to pay back 500,000 pounds or hand over his father's pub. Desperate, Eddy and his friends wait for their neighbors to rob some drug dealers, then rob the robbers in turn. After both thefts, the number of interested criminal parties increases, with the four friends in dangerously over their heads.",
                     "http://www.gstatic.com/tv/thumb/movieposters/22639/p22639_p_v8_ag.jpg",
                     "https://www.youtube.com/watch?v=Y8MXn5No1Jc")

avatar = media.Movie("Avatar",
                     "Humen invade alien planet and aliens defend",
                     "https://www.wired.com/images_blogs/underwire/2009/12/avatar_neytiri_jake_660.jpg",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")

school_of_rock = media.Movie("School of Rock",
                     "Using rock music to learn",
                     "https://static1.squarespace.com/static/560c269ae4b0c2b90045b5a4/t/5786b7546a49637b8a1793a0/1468446553014/",
                     "https://www.youtube.com/watch?v=3PsUJFEBC74")

midnight_in_paris = media.Movie("Midnight in paris",
                     "Gil Pender (Owen Wilson) is a screenwriter and aspiring novelist. Vacationing in Paris with his fiancee (Rachel McAdams), he has taken to touring the city alone. On one such late-night excursion, Gil encounters a group of strange -- yet familiar -- revelers, who sweep him along, apparently back in time, for a night with some of the Jazz Age's icons of art and literature. The more time Gil spends with these cultural heroes of the past, the more dissatisfied he becomes with the present.",
                     "https://art-s.nflximg.net/f10d0/0652fa1908d1c75e506a16f10bbab6af2ccf10d0.jpg",
                     "https://www.youtube.com/watch?v=FAfR8omt-CY")

movies = [two_smoking_barrels, avatar, school_of_rock, midnight_in_paris]
fresh_tomatoes.open_movies_page(movies)
