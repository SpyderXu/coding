double sqrt_double(double x){
    if(x < 0){
        return -1;
    }
    else if(x < 1.0){
        double l = 0;
        double r = 1;
        while(l < r){
            double mid = (l + r)/2;
            if(abs(mid*mid - x) < 1e-6){
                return mid;
            }
            else if(mid*mid > x){
                l = mid;
            }
            else{
                r = mid;
            }
        }
    }
    else{
        double l = 1;
        double r = x;
        while(l < r){
            double mid = (l + r)/2;
            if(abs(mid*mid - x) < 1e-6){
                return mid;
            }
            else if(mid*mid > x){
                r = mid;
            }
            else{
                l = mid;
            }
        }
    }
} 