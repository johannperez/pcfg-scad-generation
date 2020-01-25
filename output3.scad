union(){
    translate(v=[0, 0, 0]){
        translate(v=[6, 4, 0]){
            difference(){
                circle(r=6);
                circle(r=5);
            };
        };
    };
    translate(v=[10, 0, 0]){
        difference(){
            square(size=10);
            translate(v=[1, 1, 0]){
                square(size=8);
            };
        };
    };
};
