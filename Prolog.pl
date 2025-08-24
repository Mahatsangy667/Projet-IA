% =====================
% Types de crime
% =====================
crime_type(assassinat).
crime_type(vol).
crime_type(escroquerie).

% =====================
% Faits
% =====================
suspect(john).
suspect(mary).
suspect(alice).
suspect(bruno).
suspect(sophie).

% --- has_motive/2 ---
has_motive(john, vol).
has_motive(mary, assassinat).
has_motive(alice, escroquerie).

% --- was_near_crime_scene/2 ---
was_near_crime_scene(john, vol).
was_near_crime_scene(mary, assassinat).

% --- has_fingerprint_on_weapon/2 ---
has_fingerprint_on_weapon(john, vol).
has_fingerprint_on_weapon(mary, assassinat).

% --- has_bank_transaction/2 ---
has_bank_transaction(alice, escroquerie).
has_bank_transaction(bruno, escroquerie).

% --- owns_fake_identity/2 ---
owns_fake_identity(sophie, escroquerie).

% =====================
% Règles de culpabilité
% =====================

% --- Vol ---
is_guilty(Suspect, vol) :-
    has_motive(Suspect, vol),
    was_near_crime_scene(Suspect, vol),
    has_fingerprint_on_weapon(Suspect, vol).

% --- Assassinat ---
is_guilty(Suspect, assassinat) :-
    has_motive(Suspect, assassinat),
    was_near_crime_scene(Suspect, assassinat),
    ( has_fingerprint_on_weapon(Suspect, assassinat)
    ; eyewitness_identification(Suspect, assassinat)
    ).

% --- Escroquerie ---
is_guilty(Suspect, escroquerie) :-
    ( has_motive(Suspect, escroquerie),
      has_bank_transaction(Suspect, escroquerie)
    )
    ;
    owns_fake_identity(Suspect, escroquerie).

% =====================
% Menu interactif
% =====================
menu :-
    writeln('=============================='),
    writeln('     SYSTEME EXPERT CRIME     '),
    writeln('=============================='),
    writeln('Suspects disponibles :'),
    forall(suspect(S), (write('- '), writeln(S))),
    writeln('------------------------------'),
    writeln('Crimes possibles :'),
    forall(crime_type(C), (write('- '), writeln(C))),
    writeln('=============================='),
    writeln('Tape ton choix comme ceci:'),
    writeln('crime(nom_suspect, type_crime).'),
    writeln('Puis termine avec un point et Entrée.'),
    writeln('=============================='),
    main.

% =====================
% Entrée principale
% =====================
main :-
    current_input(Input),
    read(Input, crime(Suspect, CrimeType)),
    (   is_guilty(Suspect, CrimeType) ->
        format("Verdict : ~w est COUPABLE pour ~w.~n", [Suspect, CrimeType])
    ;   format("Verdict : ~w est NON COUPABLE pour ~w.~n", [Suspect, CrimeType])
    ),
    halt.
