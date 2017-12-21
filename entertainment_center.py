import media
import fresh_tomatoes

two_smoking_barrels = media.Movie(
                                  "Lock, stock and two smoking barrels",
                                  "Eddy (Nick Moran) convinces three friends to pool funds for a high-stakes poker game against local crime boss Hatchet Harry (P.H. Moriarty). Harry cheats and Eddy loses, giving him a week to pay back 500,000 pounds or hand over his father's pub. Desperate, Eddy and his friends wait for their neighbors to rob some drug dealers, then rob the robbers in turn. After both thefts, the number of interested criminal parties increases, with the four friends in dangerously over their heads.",
                                  "http://www.gstatic.com/tv/thumb/movieposters/22639/p22639_p_v8_ag.jpg",
                                  "https://www.youtube.com/watch?v=Y8MXn5No1Jc")

avatar = media.Movie(
                     "Avatar",
                     "Humen invade alien planet and aliens defend",
                     "https://cdn.europosters.eu/image/750/posters/avatar-limited-ed-one-sheet-sun-i7182.jpg",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")

school_of_rock = media.Movie(
                             "School of Rock",
                             "Using rock music to learn",
                             "https://static1.squarespace.com/static/560c269ae4b0c2b90045b5a4/t/5786b7546a49637b8a1793a0/1468446553014/",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")

midnight_in_paris = media.Movie(
                                "Midnight in Paris",
                                "Gil Pender (Owen Wilson) is a screenwriter and aspiring novelist. Vacationing in Paris with his fiancee (Rachel McAdams), he has taken to touring the city alone. On one such late-night excursion, Gil encounters a group of strange -- yet familiar -- revelers, who sweep him along, apparently back in time, for a night with some of the Jazz Age's icons of art and literature. The more time Gil spends with these cultural heroes of the past, the more dissatisfied he becomes with the present.",
                                "https://art-s.nflximg.net/f10d0/0652fa1908d1c75e506a16f10bbab6af2ccf10d0.jpg",
                                "https://www.youtube.com/watch?v=FAfR8omt-CY")
her = media.Movie(
                  "Her",
                  "A sensitive and soulful man earns a living by writing personal letters for other people. Left heartbroken after his marriage ends, Theodore (Joaquin Phoenix) becomes fascinated with a new operating system which reportedly develops into an intuitive and unique entity in its own right. He starts the program and meets 'Samantha' (Scarlett Johansson), whose bright voice reveals a sensitive, playful personality. Though 'friends' initially, the relationship soon deepens into love.",
                  "http://t2.gstatic.com/images?q=tbn:ANd9GcTJM7K3IleZaH3U-CDfARoFdfpB3Atg8pQqIgRkdlkAQHdMjBYH",
                  "https://www.youtube.com/watch?v=dJTU48_yghs")
mitty = media.Movie(
                    "The Secret Life of Walter Mitty",
                    "Walter Mitty (Ben Stiller), an employee at Life magazine, spends day after monotonous day developing photos for the publication. To escape the tedium, Walter inhabits a world of exciting daydreams in which he is the undeniable hero. Walter fancies a fellow employee named Cheryl (Kristen Wiig) and would love to date her, but he feels unworthy. However, he gets a chance to have a real adventure when Life's new owners send him on a mission to obtain the perfect photo for the final print issue.",
                    "http://t3.gstatic.com/images?q=tbn:ANd9GcS6vxOP7RMwBS2uVpZ5bxesRR7xNN7-6Tx6P9il7WaSayr6R4pr",
                    "https://www.youtube.com/watch?v=QD6cy4PBQPI")

movies = [two_smoking_barrels, avatar, school_of_rock,
          midnight_in_paris, her, mitty]
fresh_tomatoes.open_movies_page(movies)

