% --- Dynamic predicate to store answers ---
:- dynamic known/1.

% --- Rule base: conditions for identifying animals ---

animal(cat) :-
    verify(has_fur),
    verify(meows),
    verify(hunts_mice).

animal(dog) :-
    verify(has_fur),
    verify(barks),
    verify(wags_tail).

animal(eagle) :-
    verify(has_feathers),
    verify(flies),
    verify(has_sharp_vision).

animal(bat) :-
    verify(has_fur),
    verify(flies),
    verify(nocturnal).

animal(penguin) :-
    verify(has_feathers),
    verify(swims),
    verify(black_and_white).

% --- Verifier: asks the user unless already known ---
verify(Symptom) :-
    known(Symptom).
verify(Symptom) :-
    \+ known(_),
    ask(Symptom),
    known(Symptom).

% --- User input and storage of facts ---
ask(Question) :-
    format('Does the animal have the following characteristic: ~w? (yes/no): ', [Question]),
    read(Response),
    (Response == yes -> assertz(known(Question))
    ; true, fail).

% --- Top-level goal ---
identify :-
    retractall(known(_)),
    animal(Animal),
    format('The animal might be: ~w~n', [Animal]),
    !.
identify :-
    write('Sorry, I could not identify the animal.'), nl.

